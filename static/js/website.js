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
                if (window.innerWidth <= 960) {
                    closeMobileNav();
                }
            });
        });

        window.addEventListener("resize", function () {
            if (window.innerWidth > 960) {
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
});
