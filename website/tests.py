from unittest.mock import patch

from django.core import mail
from django.test import Client, TestCase, override_settings
from django.urls import reverse


@override_settings(EMAIL_BACKEND="django.core.mail.backends.locmem.EmailBackend")
class OpportunityPageTests(TestCase):
    enquiry_data = {
        "name": "Alex",
        "surname": "Mokoena",
        "company_name": "Example Engineering",
        "company_email": "alex@example.com",
        "company_telephone": "+27 11 555 0123",
        "message": "Please contact me about this project.",
        "website": "",
    }

    def test_requested_pages_render(self):
        for path in (
            "/",
            "/services/",
            "/projects/",
            "/opportunities/",
            "/opportunities/pv-solar-epc/",
            "/opportunities/project-capital-partners/",
            "/contact/",
        ):
            with self.subTest(path=path):
                self.assertEqual(self.client.get(path).status_code, 200)

    def test_old_epc_url_redirects_permanently(self):
        response = self.client.get("/services/pv-solar-epc/")
        self.assertEqual(response.status_code, 301)
        self.assertEqual(response["Location"], reverse("website:pv_solar_epc"))

    def test_opportunities_navigation_and_home_popup_links(self):
        response = self.client.get("/")
        html = response.content.decode()
        self.assertLess(html.index('>Projects</a>'), html.index('>Opportunities</a>'))
        self.assertLess(html.index('>Opportunities</a>'), html.index('>Contact</a>'))
        self.assertContains(response, 'href="/opportunities/pv-solar-epc/">Explore Solar EPC')
        self.assertContains(response, 'href="/opportunities/pv-solar-epc/#project-enquiry">Request an Energy Audit')

    def test_form_placeholders_are_exact(self):
        self.assertContains(
            self.client.get(reverse("website:pv_solar_epc")),
            'placeholder="I am interested in the EPC for PV Solar Solutions."',
        )
        self.assertContains(
            self.client.get(reverse("website:project_capital_partners")),
            'placeholder="I am interested in RPS Project Capital Partners."',
        )

    def test_valid_epc_enquiry(self):
        response = self.client.post(reverse("website:pv_solar_epc"), self.enquiry_data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(len(mail.outbox), 1)
        email = mail.outbox[0]
        self.assertEqual(email.to, ["projects@rpsswitchgearsa.co.za"])
        self.assertEqual(email.subject, "EPC for PV Solar Solutions – Project Enquiry")
        self.assertIn("Opportunity name: EPC for PV Solar Solutions", email.body)
        self.assertIn("Company Telephone: +27 11 555 0123", email.body)
        self.assertEqual(email.reply_to, ["alex@example.com"])
        self.assertContains(self.client.get(response["Location"]), "Thank you. Your enquiry has been sent")

    def test_invalid_epc_enquiry_does_not_send(self):
        data = {**self.enquiry_data, "company_email": "invalid", "company_telephone": "123"}
        response = self.client.post(reverse("website:pv_solar_epc"), data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Enter a valid email address")
        self.assertContains(response, "Enter a valid telephone number")
        self.assertEqual(len(mail.outbox), 0)

    def test_honeypot_rejects_enquiry(self):
        data = {**self.enquiry_data, "website": "https://spam.example"}
        response = self.client.post(reverse("website:pv_solar_epc"), data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(mail.outbox), 0)

    def test_valid_capital_partners_enquiry(self):
        response = self.client.post(reverse("website:project_capital_partners"), self.enquiry_data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(len(mail.outbox), 1)
        email = mail.outbox[0]
        self.assertEqual(email.to, ["projects@rpsswitchgearsa.co.za"])
        self.assertEqual(email.subject, "RPS Project Capital Partners – Project Enquiry")
        self.assertIn("Opportunity name: RPS Project Capital Partners", email.body)

    def test_invalid_capital_partners_enquiry_does_not_send(self):
        data = {**self.enquiry_data, "message": ""}
        response = self.client.post(reverse("website:project_capital_partners"), data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "This field is required")
        self.assertEqual(len(mail.outbox), 0)

    def test_csrf_is_required(self):
        client = Client(enforce_csrf_checks=True)
        response = client.post(reverse("website:pv_solar_epc"), self.enquiry_data)
        self.assertEqual(response.status_code, 403)

    def test_empty_submissions_validate_all_required_fields(self):
        for route in ("pv_solar_epc", "project_capital_partners"):
            with self.subTest(route=route):
                response = self.client.post(reverse(f"website:{route}"), {})
                self.assertEqual(response.status_code, 200)
                self.assertEqual(len(response.context["form"].errors), 6)
                self.assertContains(response, "This field is required")
        self.assertEqual(len(mail.outbox), 0)

    def test_email_failure_shows_generic_error(self):
        with patch("website.views.EmailMessage.send", side_effect=OSError("Private SMTP detail")):
            with self.assertLogs("website.views", level="ERROR"):
                response = self.client.post(reverse("website:pv_solar_epc"), self.enquiry_data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "We couldn&#x27;t send your enquiry. Please try again later.")
        self.assertNotContains(response, "Private SMTP detail")
        self.assertContains(response, "Example Engineering")
