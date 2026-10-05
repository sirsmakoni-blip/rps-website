document.addEventListener("DOMContentLoaded", function () {
    var navToggle = document.querySelector("[data-nav-toggle]");
    var siteNav = document.querySelector("[data-site-nav]");
    var siteHeader = document.querySelector("[data-site-header]");

    function closeMobileNav() {
        if (!navToggle || !siteNav) {
            return;
        }

        navToggle.setAttribute("aria-expanded", "false");
        siteNav.classList.remove("is-open");
    }

    if (navToggle && siteNav) {
        navToggle.addEventListener("click", function () {
            var isOpen = siteNav.classList.toggle("is-open");
            navToggle.setAttribute("aria-expanded", String(isOpen));
        });

        siteNav.querySelectorAll("a").forEach(function (link) {
            link.addEventListener("click", function () {
                if (window.innerWidth <= 1100) {
                    closeMobileNav();
                }
            });
        });

        window.addEventListener("resize", function () {
            if (window.innerWidth > 1100) {
                closeMobileNav();
            }
        });
    }

    if (siteHeader) {
        var handleScroll = function () {
            if (window.scrollY > 10) {
                siteHeader.classList.add("is-scrolled");
            } else {
                siteHeader.classList.remove("is-scrolled");
            }
        };

        handleScroll();
        window.addEventListener("scroll", handleScroll, { passive: true });
    }

    var solarAnnouncement = document.querySelector("[data-solar-announcement]");
    if (solarAnnouncement && typeof solarAnnouncement.showModal === "function") {
        var closeAnnouncement = solarAnnouncement.querySelector("[data-solar-announcement-close]");
        var previousFocus = null;

        function dismissAnnouncement() {
            if (!solarAnnouncement.open) {
                return;
            }
            solarAnnouncement.close();
            document.body.style.overflow = "";
            if (previousFocus && previousFocus.isConnected) {
                previousFocus.focus();
            }
        }

        closeAnnouncement.addEventListener("click", dismissAnnouncement);
        solarAnnouncement.addEventListener("cancel", function (event) {
            event.preventDefault();
            dismissAnnouncement();
        });
        solarAnnouncement.addEventListener("click", function (event) {
            if (event.target === solarAnnouncement) {
                dismissAnnouncement();
            }
        });
        solarAnnouncement.addEventListener("close", function () {
            document.body.style.overflow = "";
        });

        window.addEventListener("load", function () {
            window.setTimeout(function () {
                if (!solarAnnouncement.open) {
                    previousFocus = document.activeElement;
                    solarAnnouncement.showModal();
                    document.body.style.overflow = "hidden";
                    closeAnnouncement.focus();
                }
            }, 1500);
        });
    }
});
