{
    'name': "No Duplicate Followers",
    'summary': "Avoid duplicating followers when duplicating records.",
    'description': """This module provides an admin setting to activate or deactivate follower notifications upon duplication for Projects and their Tasks.""",
    'author': "Your Company",
    'website': "http://www.yourcompany.com",
    'category': 'Project',
    'version': '0.1',
    'depends': ['base', 'project'],
    'data': [
        'views/res_config_settings_views.xml',
    ],
}
