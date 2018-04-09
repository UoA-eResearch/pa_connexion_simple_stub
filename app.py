#!/usr/bin/env python3

import connexion

if __name__ == '__main__':
    app = connexion.App(__name__)
    app.add_api('swagger.yaml', validate_responses=True, arguments={'title': 'Create, view and manage e-Research projects and services used by projects.'})
    app.run(port=8080)
