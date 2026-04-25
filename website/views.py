from django.http import Http404
from django.shortcuts import render
from django.urls import reverse


COMPANY_FACTS = [
    {"value": "2008", "label": "Established"},
    {"value": "4", "label": "Core product families"},
    {"value": "6", "label": "Service lines"},
    {"value": "SA", "label": "South African base"},
]

WHY_RPS = [
    {
        "title": "Established engineering company",
        "text": "RPS Switchgear SA (Pty) Ltd is a multi faceted engineering company established in 2008.",
    },
    {
        "title": "Focused electrical capability",
        "text": "The company provides solutions and services across MV and HV switchgear, low voltage switchboard assemblies, engineering support, and electrification work.",
    },
    {
        "title": "Project and field delivery",
        "text": "Its offering extends beyond supply into construction, installation, commissioning, maintenance, and upgrade work.",
    },
    {
        "title": "Regional operating footprint",
        "text": "RPS serves utility, municipal, industrial, mining, infrastructure, and electrification projects in South Africa and the broader region.",
    },
]

ABOUT_INTRO = (
    "RPS Switchgear SA (Pty) Ltd is a multi-faceted engineering company established in 2008, "
    "providing solutions and services across medium and high voltage switchgear, low voltage "
    "switchboard assemblies, engineering support, construction, maintenance, renewable energy, "
    "and electrification."
)

ABOUT_AREAS = [
    "MV Switchgear Retrofits",
    "MV & HV Switchgear",
    "Low Voltage Switchboard Assemblies",
    "MCCs",
    "Distribution Boards",
    "Containerised Solutions",
    "MV Switchrooms",
    "LV E-Rooms",
    "Engineering & Professional Services",
    "Structural, steel and pipework fabrication, welding and erection",
    "Mechanical installation work",
    "Substation Construction",
    "Plant Construction Work, Cabling and Racking",
    "Control & Instrumentation installation work",
    "MV Switchgear & LV Systems Maintenance",
    "Township & Rural Electrification Implementation",
    "Renewable Energy Solution",
]

ABOUT_VALUES = [
    {
        "title": "Vision",
        "text": "To create a Center of Excellence for Engineering in sub-Saharan Africa.",
    },
    {
        "title": "Mission",
        "text": (
            "To achieve that vision through a proactive policy that establishes a legacy for "
            "the service life of our products, the people and companies with whom we do business."
        ),
    },
    {
        "title": "Delivery scope",
        "text": "The business combines product supply, engineering, installation, commissioning, upgrade, and maintenance capability.",
    },
    {
        "title": "Operating sectors",
        "text": "Its work spans utilities, municipalities, industrial plants, mining, renewable energy, and public electrification programmes.",
    },
]

DELIVERY_MODEL = [
    {
        "step": "01",
        "title": "Define project scope",
        "text": "Clarify the electrical requirement, plant condition, network need, and project objectives.",
    },
    {
        "step": "02",
        "title": "Engineer the solution",
        "text": "Align switchgear, retrofit, construction, installation, and protection requirements to the job.",
    },
    {
        "step": "03",
        "title": "Deliver and commission",
        "text": "Execute supply, installation, testing, and commissioning in a structured way.",
    },
    {
        "step": "04",
        "title": "Support long-term operation",
        "text": "Maintain, test, upgrade, and extend the life of electrical assets after handover.",
    },
]

SECTOR_FOCUS = [
    "Utilities and municipal power infrastructure",
    "Industrial plants and process facilities",
    "Mining and heavy industry",
    "Renewable energy projects",
    "Township and rural electrification programmes",
    "Substation construction and brownfield upgrades",
]

PRODUCT_LIFECYCLE = [
    {
        "title": "New installations",
        "text": "Product solutions for new substations, plant expansions, and fresh distribution infrastructure.",
    },
    {
        "title": "Retrofits and upgrades",
        "text": "Brownfield upgrade and retrofit work for ageing switchgear and electrical assets.",
    },
    {
        "title": "Maintenance support",
        "text": "Testing, maintenance, and protection support for long-term system reliability.",
    },
]

SERVICE_APPROACH = [
    {
        "title": "Engineering support",
        "text": "Provide professional and technical services to define the project properly.",
    },
    {
        "title": "Construction and installation",
        "text": "Deliver plant, substation, electrification, and associated electrical works on site.",
    },
    {
        "title": "Testing and commissioning",
        "text": "Carry out maintenance, protection relay testing, installation checks, and commissioning activities.",
    },
    {
        "title": "Ongoing asset support",
        "text": "Support the service life of switchgear and LV systems through maintenance and upgrades.",
    },
]

PROJECT_PRIORITIES = [
    {
        "title": "Design and build capability",
        "text": "RPS delivers projects across design, procurement, installation, construction, and commissioning scopes.",
    },
    {
        "title": "Brownfield upgrade experience",
        "text": "The project record includes retrofit and upgrade work on existing assets and substations.",
    },
    {
        "title": "Utility and industrial delivery",
        "text": "Completed work spans municipalities, mining, solar, substations, distribution boards, and electrification.",
    },
    {
        "title": "Commissioning focus",
        "text": "Projects include testing, protection, and commissioning as core delivery stages.",
    },
]

REGIONAL_PRESENCE = [
    "Jet Park, Johannesburg operational base",
    "Product, service, and project support across South Africa",
    "Regional work including Botswana, Zimbabwe, Zambia, and the DRC",
]

ENQUIRY_TOPICS = [
    "MV / HV switchgear requirements",
    "Low voltage switchboard assemblies",
    "Reyrolle retrofit scopes",
    "Substation construction or upgrade work",
    "Maintenance and protection relay testing",
    "Renewable energy and electrification projects",
]

CLIENTS = [
    "UCL Company",
    "Siemag-Tecberg",
    "AMJ Electrical",
    "Botswana Power Corporation",
    "City of Cape Town Municipality",
    "Nelson Mandela Metropolitan Municipality",
    "Gecamines - Democratic Republic of Congo",
    "Zimbabwe Electricity Transmission & Distribution Company",
    "Transnet",
    "Consolidated Power Projects",
    "Tharisa Minerals",
    "Mopani Copper Mines - Zambia",
    "NCT Forestry",
    "TWP Projects",
    "Greater Tzaneen Municipality",
    "uMhlathuze Municipality",
]

PRODUCTS = [
    {
        "slug": "assure-hmvp-switchgear",
        "name": "Assure HMVP Switchgear",
        "category": "Medium voltage switchgear",
        "image": "/static/img/assure-hmvp-switchgear.png",
        "summary": "RPS Assure HMVP Switchgear for medium voltage applications.",
        "intro": "Assure HMVP Switchgear supports medium voltage distribution, control, and protection requirements across electrical infrastructure projects.",
        "overview": (
            "This product sits within the company’s MV switchgear product range and forms part of "
            "its supply capability for industrial, utility, municipal, and infrastructure projects."
        ),
        "highlights": [
            "Part of the RPS medium voltage switchgear offering",
            "Positioned within the company’s core product range",
            "Relevant to project supply, installation, testing, and commissioning scopes",
        ],
        "applications": [
            "Substations",
            "Industrial plants",
            "Municipal and infrastructure power systems",
        ],
        "support": [
            "Engineering support",
            "Installation and commissioning support",
            "Maintenance and upgrade alignment",
        ],
        "meta": [
            {"label": "Product type", "value": "MV switchgear"},
            {"label": "Company category", "value": "Core product family"},
            {"label": "Project fit", "value": "Supply, installation, and commissioning"},
        ],
    },
    {
        "slug": "lmvp-switchgear",
        "name": "RPS LMVP Switchgear",
        "category": "LMVP switchgear",
        "image": "/static/img/lvmp.png",
        "summary": "RPS LMVP Switchgear for electrical distribution applications.",
        "intro": "RPS LMVP Switchgear supports electrical distribution requirements across industrial, municipal, and infrastructure applications.",
        "overview": (
            "The product forms part of the company’s electrical distribution offering and supports "
            "broader project work in industrial, municipal, and infrastructure environments."
        ),
        "highlights": [
            "Core RPS product line",
            "Aligned to electrical distribution projects",
            "Suited to supply and project execution packages",
        ],
        "applications": [
            "Distribution systems",
            "Industrial facilities",
            "Infrastructure and municipal environments",
        ],
        "support": [
            "Engineering and professional services support",
            "Construction and installation alignment",
            "Testing and commissioning support",
        ],
        "meta": [
            {"label": "Product type", "value": "Switchgear"},
            {"label": "Company category", "value": "Core product family"},
            {"label": "Project fit", "value": "Distribution and project delivery"},
        ],
    },
    {
        "slug": "reyrolle-retrofit-solutions",
        "name": "Reyrolle Switchgear Retrofit Solutions",
        "category": "Retrofit solutions",
        "image": "/static/img/retrofit.png",
        "summary": "Retrofit solutions for legacy Reyrolle switchgear installations.",
        "intro": "Reyrolle Switchgear Retrofit Solutions support brownfield upgrade work on existing Reyrolle installations requiring life extension and modernisation.",
        "overview": (
            "This offering supports the upgrade of existing Reyrolle switchgear assets and aligns with "
            "the company’s retrofit, relay upgrade, and replacement work shown in its project portfolio."
        ),
        "highlights": [
            "Focused on legacy Reyrolle switchgear",
            "Supports brownfield upgrade projects",
            "Aligned to retrofit and relay upgrade scopes",
        ],
        "applications": [
            "Legacy substations",
            "Brownfield upgrade projects",
            "Operational power systems requiring refurbishment",
        ],
        "support": [
            "Retrofit planning",
            "Installation and replacement support",
            "Testing and recommissioning alignment",
        ],
        "meta": [
            {"label": "Product type", "value": "Retrofit solution"},
            {"label": "Company category", "value": "Core product family"},
            {"label": "Project fit", "value": "Life extension and upgrade work"},
        ],
    },
    {
        "slug": "low-voltage-switchboard-assemblies",
        "name": "Low Voltage Switchboard Assemblies",
        "category": "LV switchboards",
        "image": "/static/img/lv_solutions.png",
        "summary": "Low voltage switchboard assemblies including MCCs, distribution boards, containerised solutions, MV switchrooms, and LV E-Rooms.",
        "intro": "Low Voltage Switchboard Assemblies support distribution, motor control, and packaged electrical infrastructure requirements across project environments.",
        "overview": (
            "The company’s LV assembly capability includes MCCs, distribution boards, containerised "
            "solutions, MV switchrooms, and LV E-Rooms for broader electrical infrastructure delivery."
        ),
        "highlights": [
            "Core RPS product family",
            "Includes MCCs and distribution boards",
            "Extends to containerised solutions, MV switchrooms, and LV E-Rooms",
        ],
        "applications": [
            "Industrial facilities",
            "Municipal projects",
            "Commercial and infrastructure electrical systems",
        ],
        "support": [
            "Engineering support",
            "Manufacture, installation, and commissioning alignment",
            "Maintenance and future upgrade support",
        ],
        "meta": [
            {"label": "Product type", "value": "LV switchboard assemblies"},
            {"label": "Company category", "value": "Core product family"},
            {"label": "Project fit", "value": "Supply, installation, and distribution systems"},
        ],
    },
]

SERVICES = [
    {
        "slug": "renewable-energy-solutions",
        "name": "Renewable Energy Solutions",
        "category": "Energy infrastructure",
        "image": "/static/img/assure-hmvp-switchgear.png",
        "summary": "Renewable energy solutions for generation, integration, and supporting electrical infrastructure.",
        "intro": "Renewable Energy Solutions support projects that require practical electrical engineering, installation, and commissioning capability.",
        "overview": (
            "The offering supports solar and related energy infrastructure projects as part of the "
            "company’s broader electrical engineering, installation, and commissioning capability."
        ),
        "scope": [
            "Renewable energy electrical infrastructure",
            "Project execution support",
            "Installation and commissioning alignment",
        ],
        "outcomes": [
            "Integrated project delivery",
            "Electrical infrastructure support",
            "Commissioning-ready implementation",
        ],
        "fit": [
            "Solar projects",
            "Hybrid power environments",
            "Energy infrastructure programmes",
        ],
        "meta": [
            {"label": "Service type", "value": "Renewable energy"},
            {"label": "Capability", "value": "Core service line"},
            {"label": "Project fit", "value": "Electrical project delivery"},
        ],
    },
    {
        "slug": "engineering-and-professional-services",
        "name": "Engineering & Professional Services",
        "category": "Technical support",
        "image": "/static/img/assure-hmvp-switchgear.png",
        "summary": "Engineering and professional services for electrical project planning and delivery.",
        "intro": "Engineering & Professional Services support project planning, technical definition, coordination, and delivery across electrical infrastructure work.",
        "overview": (
            "This service supports the planning, technical definition, and execution of electrical "
            "projects across switchgear, substations, installations, and related infrastructure."
        ),
        "scope": [
            "Technical support",
            "Project engineering",
            "Professional services for delivery planning",
        ],
        "outcomes": [
            "Clearer project definition",
            "Better technical coordination",
            "Stronger project execution support",
        ],
        "fit": [
            "Industrial projects",
            "Infrastructure delivery",
            "Switchgear and substation programmes",
        ],
        "meta": [
            {"label": "Service type", "value": "Engineering support"},
            {"label": "Capability", "value": "Core service line"},
            {"label": "Project fit", "value": "Planning and execution"},
        ],
    },
    {
        "slug": "plant-construction",
        "name": "Plant Construction Work",
        "category": "Construction delivery",
        "image": "/static/img/assure-hmvp-switchgear.png",
        "summary": "Plant construction work for industrial facilities and electrical infrastructure projects.",
        "intro": "Plant Construction Work supports site-based delivery across industrial facilities and related electrical infrastructure packages.",
        "overview": (
            "The capability includes structural, steel and pipework fabrication, "
            "mechanical installation work, cabling and racking, and control and instrumentation installation work."
        ),
        "scope": [
            "Plant construction work",
            "Mechanical installation work",
            "Cabling, racking, and control & instrumentation installation",
        ],
        "outcomes": [
            "Disciplined site execution",
            "Integrated construction delivery",
            "Support for wider electrical packages",
        ],
        "fit": [
            "Industrial plants",
            "Process facilities",
            "Infrastructure and site-based projects",
        ],
        "meta": [
            {"label": "Service type", "value": "Construction"},
            {"label": "Capability", "value": "Core service line"},
            {"label": "Project fit", "value": "Site execution and installation"},
        ],
    },
    {
        "slug": "substation-construction-and-upgrades",
        "name": "Substation Construction & Upgrade",
        "category": "Substation delivery",
        "image": "/static/img/assure-hmvp-switchgear.png",
        "summary": "Substation construction and upgrade work for utility, municipal, and industrial environments.",
        "intro": "Substation Construction & Upgrade supports utility, municipal, industrial, and infrastructure projects requiring new build or brownfield substation work.",
        "overview": (
            "The project portfolio shows both substation switchroom work and wider distribution and "
            "upgrade projects, linking this service directly to active field delivery capability."
        ),
        "scope": [
            "Substation construction",
            "Substation upgrade work",
            "Related installation and commissioning support",
        ],
        "outcomes": [
            "Improved electrical infrastructure",
            "Structured upgrade delivery",
            "Commissioning-ready substations",
        ],
        "fit": [
            "Municipal projects",
            "Utility projects",
            "Industrial substations",
        ],
        "meta": [
            {"label": "Service type", "value": "Substation works"},
            {"label": "Capability", "value": "Core service line"},
            {"label": "Project fit", "value": "Build and upgrade programmes"},
        ],
    },
    {
        "slug": "maintenance-and-protection-relay-testing",
        "name": "Maintenance & Protection Relay Testing",
        "category": "Testing and asset care",
        "image": "/static/img/assure-hmvp-switchgear.png",
        "summary": "Maintenance and protection relay testing for switchgear and electrical systems.",
        "intro": "Maintenance & Protection Relay Testing supports the reliable performance of switchgear and electrical systems in service.",
        "overview": (
            "The service forms part of the company’s wider asset support offering across MV switchgear, "
            "LV systems, testing, maintenance, and lifecycle reliability."
        ),
        "scope": [
            "Protection relay testing",
            "MV switchgear maintenance",
            "LV systems maintenance",
        ],
        "outcomes": [
            "Support for ongoing asset performance",
            "Improved testing and maintenance coverage",
            "Better lifecycle support for installed systems",
        ],
        "fit": [
            "Operational substations",
            "Industrial plants",
            "Existing electrical infrastructure",
        ],
        "meta": [
            {"label": "Service type", "value": "Maintenance and testing"},
            {"label": "Capability", "value": "Core service line"},
            {"label": "Project fit", "value": "In-service asset support"},
        ],
    },
    {
        "slug": "township-and-rural-electrification",
        "name": "Township & Rural Electrification Implementation",
        "category": "Electrification delivery",
        "image": "/static/img/assure-hmvp-switchgear.png",
        "summary": "Township and rural electrification implementation for community and public infrastructure projects.",
        "intro": "Township & Rural Electrification Implementation supports network rollout projects that extend access to reliable electrical infrastructure.",
        "overview": (
            "This service is strongly reflected in the company’s project portfolio, including turnkey "
            "electrification work involving design, construction, and commissioning of electrical networks."
        ),
        "scope": [
            "Electrification implementation",
            "Network construction",
            "Commissioning and handover support",
        ],
        "outcomes": [
            "Expanded electrical access",
            "Structured rollout delivery",
            "Network commissioning and operational handover",
        ],
        "fit": [
            "Township projects",
            "Rural electrification programmes",
            "Public infrastructure rollouts",
        ],
        "meta": [
            {"label": "Service type", "value": "Electrification"},
            {"label": "Capability", "value": "Core service line"},
            {"label": "Project fit", "value": "Community and public infrastructure"},
        ],
    },
]

PROJECTS = [
    {
        "sector": "Retrofits",
        "title": "BPC - Botswana Power Corporation",
        "image": "/static/img/switchgear-room.png",
        "summary": (
            "Retrofitting of a 14-panel switchboard at Selibe Phikwe Substation in Botswana."
        ),
        "deliverables": [
            "Retrofitting of 14-panel switchboard",
            "Substation upgrade support",
            "Site execution in Selibe Phikwe, Botswana",
        ],
    },
    {
        "sector": "Retrofits",
        "title": "ZETDC - Zimbabwe",
        "image": "/static/img/retrofit.png",
        "summary": (
            "Retrofitting of a 14-panel switchboard at Mount Hampden Substation in Zimbabwe."
        ),
        "deliverables": [
            "Retrofitting of 14-panel switchboard",
            "Substation retrofit support",
            "Site execution in Mount Hampden, Zimbabwe",
        ],
    },
    {
        "sector": "Renewable energy",
        "title": "Quton Farms - Bronkhorstspruit, South Africa",
        "image": "/static/img/solar_1.png",
        "summary": (
            "100kW, 200 PV hybrid solar power solution for Quton Farms in Bronkhorstspruit, South Africa."
        ),
        "deliverables": [
            "100kW hybrid solar power solution",
            "200 PV solar plant installation",
            "Renewable energy system support",
        ],
    },
    {
        "sector": "Renewable energy",
        "title": "Clyde Steel Solar Power Plant",
        "image": "/static/img/clyde.png",
        "summary": (
            "A 400kW solar power plant project involving design, procurement, installation and commissioning "
            "for a steel manufacturing company in Springs, Gauteng."
        ),
        "deliverables": [
            "Design",
            "Procurement",
            "Installation and commissioning",
        ],
    },
    {
        "sector": "MV reticulation",
        "title": "Greengate MV Electrical Reticulation",
        "image": "/static/img/greengate.png",
        "summary": (
            "Design, construction and commissioning of an MV electrical network to supply electricity "
            "to a new development."
        ),
        "deliverables": [
            "Installation of three MV underground cables from Eskom’s Dalkeith Substation over about 4.6km",
            "Supply and installation of ring main units and three 500kVA mini-subs",
            "Delivery to Eskom standards and handover on completion",
        ],
    },
    {
        "sector": "Electrification",
        "title": "Tarlton Matshela Pata Electrification",
        "image": "/static/img/assure-hmvp-switchgear.png",
        "summary": (
            "A turnkey electrification project involving design, construction and commissioning of "
            "an electrical network benefiting 1317 families in an informal settlement."
        ),
        "deliverables": [
            "11kV MV network construction",
            "Installation of 19 x 200kVA pole mounted transformers",
            "More than 11 000 metres of ABC bundled LV conductor network, Airdac house connections, and split meter installation and commissioning",
        ],
    },
    {
        "sector": "Substation and switchroom",
        "title": "Tharisa Mine Substation Switchroom",
        "image": "/static/img/assure-hmvp-switchgear.png",
        "summary": (
            "Design and construction of a substation switchroom including protection schemes and "
            "installation and commissioning of 12 MV switchgear panels."
        ),
        "deliverables": [
            "Switchroom design and construction",
            "Protection schemes based on ABB relays",
            "Installation and commissioning of 12 MV switchgear panels of RPS Switchgear HMVP Assure Panels",
        ],
    },
    {
        "sector": "Retrofits",
        "title": "ZETDC Coventry Reyrolle Retrofit",
        "image": "/static/img/assure-hmvp-switchgear.png",
        "summary": (
            "Retrofitting of legacy Reyrolle switchgear and protection relay upgrade for ZETDC Coventry."
        ),
        "deliverables": [
            "Replacement of SF6 breakers with vacuum circuit breakers across a 15-panel switchboard",
            "Replacement of old electromechanical relays with IED relays",
            "Replacement of faulty CTs and VTs plus supply and installation of two extension panels and a new bus section panel",
        ],
    },
    {
        "sector": "Motor control centres",
        "title": "City of uMhlathuze Municipality Pump Stations MCCs",
        "image": "/static/img/assure-hmvp-switchgear.png",
        "summary": (
            "Design, manufacture, installation and commissioning of motor control centres for pump stations, "
            "built in the RPS workshop in Jet Park, Boksburg."
        ),
        "deliverables": [
            "Design",
            "Manufacture",
            "Installation and commissioning",
        ],
    },
    {
        "sector": "LV distribution",
        "title": "Wilmar Processing SA Outdoor Distribution Board",
        "image": "/static/img/assure-hmvp-switchgear.png",
        "summary": "Design, supply and delivery of a 1600A rated outdoor distribution board for Wilmar Processing SA (Pty) Ltd.",
        "deliverables": [
            "Design",
            "Supply",
            "Delivery",
        ],
    },
    {
        "sector": "Substation upgrade",
        "title": "Gecamines Kolwezi SS Upgrade",
        "image": "/static/img/assure-hmvp-switchgear.png",
        "summary": "Manufacture, supply and delivery of 32 panels of 6.6kV 25-kA SBB switchboard to Gecamines Kolwezi Substation, DRC.",
        "deliverables": [
            "Manufacture",
            "Supply",
            "Delivery",
        ],
    },
    {
        "sector": "Substation equipment",
        "title": "Drakenstein Municipality Suid-End Substation",
        "image": "/static/img/assure-hmvp-switchgear.png",
        "summary": "Supply, installation and commissioning of 66kV circuit breakers and control panels for Suid-End Substation, Drakenstein.",
        "deliverables": [
            "Supply",
            "Installation",
            "Commissioning",
        ],
    },
    {
        "sector": "Solar lighting",
        "title": "Zimbabwe Ezekiel Guti University Solar Street Lights",
        "image": "/static/img/assure-hmvp-switchgear.png",
        "summary": "Supply and installation of solar street lights at Zimbabwe Ezekiel Guti University, Zimbabwe.",
        "deliverables": [
            "Supply",
            "Installation",
        ],
    },
]

CONTACT_DETAILS = [
    {
        "label": "Address",
        "value": "33 Kelly Road, Unit 4 Meerzicht Business Park, Jet Park, 1459, Johannesburg",
        "note": "",
    },
    {
        "label": "Email",
        "value": "sales@rpsswitchgearsa.co.za",
        "note": "",
    },
    {
        "label": "Telephone",
        "value": "+27 11 392 1640",
        "note": "",
    },
    {
        "label": "Working Hours",
        "value": "",
        "note": "",
        "hours": [
            {"day": "Monday - Thursday", "time": "07:30 - 16:30"},
            {"day": "Friday", "time": "07:30 - 14:30"},
            {"day": "Weekends", "time": "Closed"},
        ],
    },
]

PRODUCT_LOOKUP = {product["slug"]: product for product in PRODUCTS}
SERVICE_LOOKUP = {service["slug"]: service for service in SERVICES}
ABOUT_IMAGE = "/static/img/about.png"
SERVICES_IMAGE = "/static/img/service.png"
PROJECTS_IMAGE = "/static/img/projects.png"
CONTACT_IMAGE = "/static/img/contact.png"

def make_breadcrumbs(*crumbs):
    trail = [{"label": "Home", "url": reverse("website:home")}]
    trail.extend(crumbs)
    return trail


def make_cta(
    title,
    text,
    eyebrow="Next step",
    primary_label="Contact Us",
    secondary_label=None,
    secondary_url=None,
):
    return {
        "eyebrow": eyebrow,
        "title": title,
        "text": text,
        "primary_label": primary_label,
        "primary_url": reverse("website:contact"),
        "secondary_label": secondary_label,
        "secondary_url": secondary_url,
    }


def base_context(active_page, **kwargs):
    context = {
        "active_page": active_page,
        "contact_details": CONTACT_DETAILS,
        "footer_products": PRODUCTS,
        "footer_services": SERVICES[:4],
    }
    context.update(kwargs)
    return context


def get_item_or_404(mapping, slug, item_name):
    item = mapping.get(slug)
    if item is None:
        raise Http404(f"{item_name} not found.")
    return item


def home(request):
    context = base_context(
        "home",
        company_facts=COMPANY_FACTS,
        why_rps=WHY_RPS,
        featured_products=PRODUCTS,
        featured_services=SERVICES,
        projects_preview=PROJECTS[:6],
        sector_focus=SECTOR_FOCUS,
        clients=CLIENTS,
        hero_title="Electrical Engineering, Switchgear and Infrastructure Solutions",
        hero_text=(
            "RPS Switchgear SA (Pty) Ltd is a multi-faceted engineering company established in 2008, "
            "providing switchgear, engineering, construction, maintenance, retrofit, renewable energy, and electrification solutions."
        ),
        cta=make_cta(
            eyebrow="Get in touch",
            title="Talk to RPS Switchgear SA about your next electrical project.",
            text="Contact the team for switchgear, retrofit, construction, maintenance, testing, renewable energy, and electrification enquiries.",
            primary_label="Contact RPS",
            secondary_label="View projects",
            secondary_url=reverse("website:projects"),
        ),
    )
    return render(request, "website/home.html", context)


def about(request):
    context = base_context(
        "about",
        breadcrumbs=make_breadcrumbs({"label": "About"}),
        about_intro=ABOUT_INTRO,
        about_areas=ABOUT_AREAS,
        about_values=ABOUT_VALUES,
        about_image=ABOUT_IMAGE,
        delivery_model=DELIVERY_MODEL,
        sector_focus=SECTOR_FOCUS,
        cta=make_cta(
            title="Looking for an established electrical engineering partner?",
            text="RPS Switchgear SA combines product supply, engineering support, installation, commissioning, maintenance, and upgrade capability.",
            primary_label="Contact the team",
            secondary_label="Explore services",
            secondary_url=reverse("website:services"),
        ),
    )
    return render(request, "website/about.html", context)


def products(request):
    context = base_context(
        "products",
        breadcrumbs=make_breadcrumbs({"label": "Products"}),
        products=PRODUCTS,
        lifecycle_stages=PRODUCT_LIFECYCLE,
        cta=make_cta(
            title="Explore the RPS product range.",
            text="Browse switchgear, retrofit solutions, and low voltage assemblies that form the company’s core product offering.",
            primary_label="Speak to RPS",
            secondary_label="View services",
            secondary_url=reverse("website:services"),
        ),
    )
    return render(request, "website/products.html", context)


def product_detail(request, slug):
    product = get_item_or_404(PRODUCT_LOOKUP, slug, "Product")
    related_products = [item for item in PRODUCTS if item["slug"] != slug][:3]
    context = base_context(
        "products",
        product=product,
        related_products=related_products,
        breadcrumbs=make_breadcrumbs(
            {"label": "Products", "url": reverse("website:products")},
            {"label": product["name"]},
        ),
        cta=make_cta(
            title="Need more information on this product?",
            text="Contact RPS Switchgear SA to discuss project fit, engineering requirements, supply, installation, testing, or upgrade scope.",
            primary_label="Request information",
            secondary_label="Browse all products",
            secondary_url=reverse("website:products"),
        ),
    )
    return render(request, "website/product_detail.html", context)


def services(request):
    context = base_context(
        "services",
        breadcrumbs=make_breadcrumbs({"label": "Services"}),
        services=SERVICES,
        service_approach=SERVICE_APPROACH,
        services_image=SERVICES_IMAGE,
        cta=make_cta(
            title="Explore the RPS services offering.",
            text="From engineering support to construction, maintenance, relay testing, renewable energy, and electrification, RPS covers a broad electrical project scope.",
            primary_label="Contact the team",
            secondary_label="View projects",
            secondary_url=reverse("website:projects"),
        ),
    )
    return render(request, "website/services.html", context)


def service_detail(request, slug):
    service = get_item_or_404(SERVICE_LOOKUP, slug, "Service")
    related_services = [item for item in SERVICES if item["slug"] != slug][:3]
    context = base_context(
        "services",
        service=service,
        related_services=related_services,
        breadcrumbs=make_breadcrumbs(
            {"label": "Services", "url": reverse("website:services")},
            {"label": service["name"]},
        ),
        cta=make_cta(
            title="Need this service on a current or upcoming project?",
            text="Contact RPS Switchgear SA to discuss your requirements and project scope.",
            primary_label="Discuss your project",
            secondary_label="See all services",
            secondary_url=reverse("website:services"),
        ),
    )
    return render(request, "website/service_detail.html", context)


def projects(request):
    context = base_context(
        "projects",
        breadcrumbs=make_breadcrumbs({"label": "Projects"}),
        projects=PROJECTS,
        project_priorities=PROJECT_PRIORITIES,
        projects_image=PROJECTS_IMAGE,
        cta=make_cta(
            title="See how RPS Switchgear SA has delivered across electrification, substations, retrofit, solar, and distribution projects.",
            text="The portfolio includes work in South Africa and the broader region across utility, industrial, mining, and public infrastructure environments.",
            primary_label="Contact RPS",
            secondary_label="Explore products",
            secondary_url=reverse("website:products"),
        ),
    )
    return render(request, "website/projects.html", context)


def contact(request):
    context = base_context(
        "contact",
        breadcrumbs=make_breadcrumbs({"label": "Contact"}),
        enquiry_topics=ENQUIRY_TOPICS,
        regional_presence=REGIONAL_PRESENCE,
        contact_image=CONTACT_IMAGE,
        cta=make_cta(
            title="Get in touch with RPS Switchgear SA.",
            text="Use the contact details on this page to enquire about products, services, and project opportunities.",
            primary_label="Contact RPS",
        ),
    )
    return render(request, "website/contact.html", context)
