# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v1.11.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import kubernetes_asyncio.client
from kubernetes_asyncio.client.api.version_api import VersionApi  # noqa: E501
from kubernetes_asyncio.client.rest import ApiException


class TestVersionApi(unittest.TestCase):
    """VersionApi unit test stubs"""

    def setUp(self):
        self.api = kubernetes_asyncio.client.api.version_api.VersionApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_code(self):
        """Test case for get_code

        """
        pass


if __name__ == '__main__':
    unittest.main()
