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

CONTACT_ADDRESS = "33 Kelly Road, Unit 4 Meerzicht Business Park, Jet Park, 1459, Johannesburg"
CONTACT_MAP_URL = "https://www.google.com/maps/search/?api=1&query=33+Kelly+Road+Jet+Park+Boksburg"
CONTACT_EMAIL = "sales@rpsswitchgearsa.co.za"
CONTACT_PHONE_DISPLAY = "+27 11 392 1640"
CONTACT_PHONE_URI = "+27113921640"
CONTACT_WORKING_HOURS = [
    {"day": "Mon–Thu", "time": "07:30–16:30"},
    {"day": "Fri", "time": "07:30–14:30"},
    {"day": "Weekends", "time": "Closed"},
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
        "category": "Horizontal indoor MV switchgear",
        "image": "/static/img/assure-hmvp-switchgear.webp",
        "summary": "IEC-certified horizontal indoor switchgear with a 31.5kA for 1 second A-FLR internal arc rating to IEC 62271.",
        "intro": "RPS Switchgear's Assure range of Horizontal Indoor Switchgear is fully type tested and certified to international IEC Standards. With an impressive internal arc rating of 31.5kA for 1 second A-FLR to IEC 62271, it will more than satisfy the most demanding of network owners' requirements.",
        "overview": (
            "As part of the RPS medium voltage range, Assure HMVP is positioned for projects that "
            "need robust indoor switchgear, proven standards compliance, and dependable performance "
            "across utility, municipal, mining, and industrial networks."
        ),
        "highlights": [
            "Horizontal Indoor Switchgear",
            "Fully type tested",
            "Certified to IEC Standards",
            "Internal arc rating: 31.5kA for 1 second A-FLR to IEC 62271",
            "Suitable for demanding network owner requirements",
        ],
        "applications": [
            "Utility and municipal substations",
            "Industrial and mining power systems",
            "Indoor medium voltage switchrooms",
        ],
        "support": [
            "Engineering support",
            "Installation and commissioning support",
            "Maintenance and upgrade alignment",
        ],
        "meta": [
            {"label": "Product type", "value": "Horizontal indoor switchgear"},
            {"label": "Certification", "value": "IEC Standards"},
            {"label": "Internal arc rating", "value": "31.5kA for 1 second A-FLR to IEC 62271"},
        ],
        "brochure": "brochures/assure-hmvp-switchgear-brochure.pdf",
        "brochure_label": "Download Assure HMVP Brochure",
    },
    {
        "slug": "lmvp-switchgear",
        "name": "RPS LMVP Switchgear",
        "category": "Medium voltage switchgear",
        "image": "/static/img/lvmp.webp",
        "summary": "Medium voltage switchgear for network distribution with five breaker current ratings from 630/800A through 2500A.",
        "intro": "The LMVP switchgear enables the distribution of Electrical Power through Networks to the Consumer at medium voltage. The circuit breakers are available in 5 current ratings, 630/800A, 630A cap switching, 1250A, 2000A and 2500A.",
        "overview": (
            "The LMVP range supports medium voltage distribution duties where project teams need "
            "rating flexibility and a practical switchgear platform for municipal, industrial, "
            "mining, and infrastructure applications."
        ),
        "highlights": [
            "Medium voltage power distribution",
            "5 current ratings",
            "630/800A",
            "630A cap switching",
            "1250A",
            "2000A",
            "2500A",
        ],
        "applications": [
            "Medium voltage distribution networks",
            "Industrial and mining facilities",
            "Municipal and infrastructure environments",
        ],
        "support": [
            "Engineering and professional services support",
            "Construction and installation alignment",
            "Testing and commissioning support",
        ],
        "meta": [
            {"label": "Product type", "value": "Medium voltage switchgear"},
            {"label": "Available ratings", "value": "630/800A, 630A cap switching, 1250A, 2000A, 2500A"},
            {"label": "Project fit", "value": "Distribution and network delivery"},
        ],
        "brochure": "brochures/lmvp-switchgear-brochure.pdf",
        "brochure_label": "Download LMVP Brochure",
    },
    {
        "slug": "reyrolle-retrofit-solutions",
        "name": "Reyrolle Switchgear Retrofit Solutions",
        "category": "Legacy switchgear retrofit solutions",
        "image": "/static/img/retrofit.webp",
        "summary": "Type-tested retrofit and extension solutions for legacy Reyrolle LM switchgear that improve safety and service life without full switchboard replacement.",
        "intro": "RPS Switchgear SA provides retrofit solutions for the legacy Reyrolle LM range of switchgear, which has an enormous installed base in Sub-Saharan Africa. RPS Switchgear SA is in a position to upgrade and retrofit existing legacy switchgear to IEC 62271-100/200 safety features. RPS SA also provides LMVP extension panels for legacy Reyrolle switchboards that are certified to a 25kA at 1 second A-FLR IAC withstand and seismic 1G test.",
        "overview": (
            "This offering provides a practical modernization path for operators who need to extend the "
            "service life of installed Reyrolle switchgear while improving safety, reliability, "
            "maintainability, and operational continuity. By retrofitting compatible existing "
            "switchboard infrastructure rather than replacing complete boards, projects can strengthen "
            "performance and reduce the disruption associated with full switchboard replacement."
        ),
        "highlights": [
            "Retrofit solutions for legacy Reyrolle LM switchgear",
            "Extends service life without full switchboard replacement",
            "Upgrades existing installations toward IEC 62271-100/200 safety features",
            "Compatible with existing switchgear infrastructure where applicable",
            "LMVP extension panels certified to 25kA at 1 second A-FLR IAC withstand",
            "Supports improved reliability, maintainability, safety, and operational continuity",
        ],
        "applications": [
            "Legacy Reyrolle switchboards in service",
            "Brownfield substation and plant upgrades",
            "Operational networks requiring life extension and modernization",
        ],
        "support": [
            "Retrofit planning and scope definition",
            "Installation aligned to existing switchgear infrastructure",
            "Testing, recommissioning, and upgrade support",
        ],
        "meta": [
            {"label": "Product type", "value": "Legacy switchgear retrofit solution"},
            {"label": "Safety upgrade", "value": "IEC 62271-100/200 features"},
            {"label": "Extension panel rating", "value": "25kA at 1 second A-FLR IAC withstand"},
            {"label": "Additional qualification", "value": "Seismic 1G test"},
        ],
        "brochure": "brochures/reyrolle-retrofit-solutions-brochure.pdf",
        "brochure_label": "Download Reyrolle Retrofit Solutions Brochure",
    },
    {
        "slug": "low-voltage-switchboard-assemblies",
        "name": "Low Voltage Switchboard Assemblies",
        "category": "Type-tested LV switchboard assemblies",
        "image": "/static/img/lv_solutions.webp",
        "summary": "IEC 61439 type-tested low voltage switchboard assemblies for dependable electrical distribution, motor control, and packaged plant support.",
        "intro": "RPS Switchgear SA offers Low Voltage switchboard assemblies type tested to IEC61439, including MCCs, Distribution Boards, Containerised Solutions, MV Switchrooms, and LV E-Rooms.",
        "overview": (
            "RPS supplies and manufactures low voltage switchboard assemblies for projects that require "
            "dependable electrical distribution and control, quality assembly, maintainability, and "
            "long-term operational reliability. The range is suited to commercial, industrial, "
            "municipal, and infrastructure environments where safe and practical LV distribution "
            "solutions must integrate cleanly with broader project delivery."
        ),
        "highlights": [
            "Type tested to IEC61439",
            "Supplied and manufactured by RPS Switchgear SA",
            "Supports dependable electrical distribution and control",
            "Includes MCCs, Distribution Boards, Containerised Solutions, MV Switchrooms, and LV E-Rooms",
            "Designed for safety, maintainability, and long-term operational reliability",
        ],
        "applications": [
            "Commercial facilities and buildings",
            "Industrial plants and process environments",
            "Municipal, utility, and infrastructure projects",
        ],
        "support": [
            "Engineering and assembly support",
            "Manufacture, installation, and commissioning alignment",
            "Maintenance, lifecycle support, and future upgrade readiness",
        ],
        "meta": [
            {"label": "Product type", "value": "Low voltage switchboard assemblies"},
            {"label": "Standard", "value": "IEC61439"},
            {"label": "Configurations", "value": "MCCs, Distribution Boards, Containerised Solutions, MV Switchrooms, LV E-Rooms"},
            {"label": "Project fit", "value": "Electrical distribution and control systems"},
        ],
        "brochure": None,
        "brochure_label": None,
    },
]

SERVICES = [
    {
        "slug": "renewable-energy-solutions",
        "name": "Renewable Energy Solutions",
        "category": "Energy infrastructure",
        "image": "/static/img/solar_2.webp",
        "image_mobile": "/static/img/solar_2-mobile.webp",
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
        "category": "Engineering and project support",
        "image": "/static/img/services/engineering-professional-services-1.webp",
        "summary": "Electrical engineering studies, design support, and professional services for network planning, system analysis, and power infrastructure delivery.",
        "list_summary": "Engineering studies, design support, and professional services for electrical infrastructure planning and project delivery.",
        "intro": "RPS provides Engineering Services covering load flow studies, harmonic studies, network design, protection schemes design, control systems design, MV & HV breaker maintenance and testing, and protection relay testing.",
        "overview": (
            "The professional services scope extends into master planning, project-specific planning "
            "and design, project management, and implementation support for power system "
            "infrastructure associated with major distribution, township and rural reticulation and "
            "electrification networks, including substations, overhead lines, electrification "
            "refurbishment, and cabled networks. An integral part of this work is accurate modelling "
            "of existing and future network configurations and load characteristics to enable "
            "effective network analysis using DigSilent software and ReticMaster voltage-drop models."
        ),
        "scope": [
            "Load flow and harmonic studies",
            "Network, protection scheme, and control system design",
            "MV & HV breaker maintenance and testing",
            "Protection relay testing",
            "Master planning, project-specific planning, and project management",
            "HVAC, small power and lighting, and PV system design",
        ],
        "outcomes": [
            "Accurate modelling of existing and future network configurations",
            "Better definition of plant, line parameter, and load behaviour",
            "Load flow analysis",
            "Fault level calculations",
            "Voltage stability analysis",
            "Transient switching studies",
            "Optimal placing of compensation devices",
            "Losses optimisation",
            "Quality of supply analysis",
            "Unbalanced network loading and statistical modelling of LV systems",
        ],
        "fit": [
            "Major distribution and power system infrastructure projects",
            "Township and rural reticulation and electrification networks",
            "Substations, overhead lines, refurbishment, and cabled networks",
            "Industrial, municipal, utility, and infrastructure programmes",
        ],
        "list_fit": [
            "Major distribution infrastructure projects",
            "Reticulation and electrification networks",
            "Substations, overhead lines, and cabled networks",
        ],
        "meta": [
            {"label": "Service type", "value": "Engineering and professional services"},
            {"label": "Core studies", "value": "Load flow, harmonic, fault, and voltage stability"},
            {"label": "Design scope", "value": "Network, protection, control, HVAC, lighting, and PV"},
            {"label": "Analysis tools", "value": "DigSilent and ReticMaster"},
        ],
        "images": [
            {
                "src": "/static/img/services/engineering-professional-services-1.webp",
                "alt": "Engineering studies and system schematics",
                "caption": "Engineering studies, network design, and protection planning support.",
            },
            {
                "src": "/static/img/services/engineering-professional-services-2.webp",
                "alt": "Professional services planning schematic",
                "caption": "Planning, design coordination, and professional project support for power infrastructure.",
            },
            {
                "src": "/static/img/services/engineering-professional-services-3.webp",
                "alt": "Electrical network analysis schematic",
                "caption": "Detailed network analysis using modelling tools to evaluate system performance.",
            },
        ],
    },
    {
        "slug": "plant-construction",
        "name": "Plant Construction Work",
        "category": "Construction delivery",
        "image": "/static/img/assure-hmvp-switchgear.webp",
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
        "name": "Substation Construction & Upgrades",
        "category": "Turnkey substation delivery",
        "image": "/static/img/services/substation-construction-upgrades-hero.webp",
        "summary": "Turnkey substation construction and rehabilitation for substations up to 132kV.",
        "list_summary": "Turnkey substation construction and rehabilitation support for utility, municipal, and industrial networks up to 132kV.",
        "intro": (
            "RPS Switchgear SA offers turnkey solutions in substation construction and rehabilitation "
            "for substations up to 132kV, supported by expertise in substation design, engineering, "
            "and construction."
        ),
        "overview": (
            "With more than 15 years of hands-on experience, the team delivers new-build, upgrade, "
            "and refurbishment programmes that require disciplined site-based execution, electrical "
            "infrastructure coordination, and structured commissioning support. The service is suited "
            "to projects where existing substations must be rehabilitated or expanded without losing "
            "focus on safety, maintainability, and long-term operating reliability."
        ),
        "scope": [
            "Turnkey substation construction up to 132kV",
            "Substation rehabilitation, refurbishment, and upgrade works",
            "Substation design, engineering, and construction support",
            "Associated MV/LV infrastructure and site-based electrical works",
            "Testing, commissioning, and project handover support",
        ],
        "outcomes": [
            "Construction-ready and commissioning-ready substations",
            "Improved condition and service life of existing substation assets",
            "Safer, more maintainable infrastructure for long-term operation",
            "Controlled project execution from engineering through site delivery",
        ],
        "fit": [
            "Municipal projects",
            "Utility projects",
            "Industrial substations",
            "Brownfield rehabilitation and expansion programmes",
        ],
        "list_fit": [
            "Municipal projects",
            "Utility projects",
            "Industrial substations",
        ],
        "meta": [
            {"label": "Service type", "value": "Turnkey substation works"},
            {"label": "Voltage scope", "value": "Substations up to 132kV"},
            {"label": "Delivery model", "value": "Construction, rehabilitation, and upgrades"},
        ],
    },
    {
        "slug": "maintenance-and-protection-relay-testing",
        "name": "Maintenance & Protection Relay Testing",
        "category": "Testing and asset care",
        "image": "/static/img/assure-hmvp-switchgear.webp",
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
        "image": "/static/img/assure-hmvp-switchgear.webp",
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
        "image": "/static/img/switchgear-room.webp",
        "summary": (
            "Refurbishment of a 14-panel switchboard at Selibe Phikwe Substation in Botswana."
        ),
        "deliverables": [
            "Refurbishment of 14-panel switchboard",
            "Substation upgrade support",
            "Site execution in Selibe Phikwe, Botswana",
        ],
    },
    {
        "sector": "Retrofits",
        "title": "ZETDC - Zimbabwe",
        "image": "/static/img/retrofit.webp",
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
        "image": "/static/img/solar_1.webp",
        "summary": (
            "100kW hybrid solar power solution for Quton Farms in Bronkhorstspruit, South Africa."
        ),
        "deliverables": [
            "100kW hybrid solar power solution",
            "200 PV solar plant installation",
            "Renewable energy system support",
        ],
    },
    {
        "sector": "Renewable energy",
        "title": "Clyde Steel 400kW Solar PV Plant",
        "image": "/static/img/clyde.webp",
        "summary": (
            "This 400kW solar PV project included the design, procurement, installation, and commissioning of a commercial solar power solution."
            " The project was executed in Springs, Gauteng, South Africa"
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
        "image": "/static/img/greengate.webp",
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
        "image": "/static/img/assure-hmvp-switchgear.webp",
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
        "image": "/static/img/assure-hmvp-switchgear.webp",
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
        "image": "/static/img/assure-hmvp-switchgear.webp",
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
        "image": "/static/img/assure-hmvp-switchgear.webp",
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
        "image": "/static/img/assure-hmvp-switchgear.webp",
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
        "image": "/static/img/assure-hmvp-switchgear.webp",
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
        "image": "/static/img/assure-hmvp-switchgear.webp",
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
        "image": "/static/img/assure-hmvp-switchgear.webp",
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
        "value": CONTACT_ADDRESS,
        "href": CONTACT_MAP_URL,
        "external": True,
        "note": "",
    },
    {
        "label": "Email",
        "value": CONTACT_EMAIL,
        "href": f"mailto:{CONTACT_EMAIL}",
        "note": "",
    },
    {
        "label": "Telephone",
        "value": CONTACT_PHONE_DISPLAY,
        "href": f"tel:{CONTACT_PHONE_URI}",
        "note": "",
    },
    {
        "label": "Working Hours",
        "value": "",
        "note": "",
        "hours": CONTACT_WORKING_HOURS,
    },
]

PRODUCT_LOOKUP = {product["slug"]: product for product in PRODUCTS}
SERVICE_LOOKUP = {service["slug"]: service for service in SERVICES}
ABOUT_IMAGE = "/static/img/about.webp"
SERVICES_IMAGE = "/static/img/service.webp"
SERVICES_IMAGE_MOBILE = "/static/img/service-mobile.webp"
PROJECTS_IMAGE = "/static/img/projects.webp"
PROJECTS_IMAGE_MOBILE = "/static/img/projects-mobile.webp"
CONTACT_IMAGE = "/static/img/contact.webp"
CONTACT_IMAGE_MOBILE = "/static/img/contact-mobile.webp"

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
        "contact_address": CONTACT_ADDRESS,
        "contact_email": CONTACT_EMAIL,
        "contact_phone_display": CONTACT_PHONE_DISPLAY,
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
        services_image_mobile=SERVICES_IMAGE_MOBILE,
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
        projects_image_mobile=PROJECTS_IMAGE_MOBILE,
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
        contact_image_mobile=CONTACT_IMAGE_MOBILE,
        cta=make_cta(
            title="Get in touch with RPS Switchgear SA.",
            text="Use the contact details on this page to enquire about products, services, and project opportunities.",
            primary_label="Contact RPS",
        ),
    )
    return render(request, "website/contact.html", context)
