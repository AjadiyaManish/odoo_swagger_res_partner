{
    'name': 'odoo_swagger_res_partner',
    'version': '1.0.0',
    'category': 'Tools',
    'summary': 'Test res.partner CRUD via simple JSON APIs and host web app',
    'description': """
        <h3>Odoo Swagger - Res Partner API Tester</h3>
        <p>
            This module provides a lightweight Swagger-style interface to test
            <strong>res.partner</strong> CRUD operations using simple JSON APIs.
        </p>
        <p>
            It also hosts a small web application for interacting with these endpoints
            from the browser without external tools.
        </p>
    """,
    'author': 'Envision Technolabs',
    'maintainer': 'Envision Technolabs',
    'website': 'https://www.envisiontechnolabs.com',
    'license': 'LGPL-3',
    'depends': ['base'],
    'data': [],
    # App Store requires image in static/description — not static/src
    'images': ['static/description/icon.png'],
    'installable': True,
    'application': False,
    'auto_install': False,
}