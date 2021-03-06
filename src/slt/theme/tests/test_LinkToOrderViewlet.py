from slt.theme.browser.interfaces import ILinkToOrderViewlet
from slt.theme.browser.viewlet import LinkToOrderViewlet
from slt.theme.tests.base import IntegrationTestCase

import mock


class LinkToOrderViewletTestCase(IntegrationTestCase):
    """TestCase for LinkToOrderViewlet"""

    def test_subclass(self):
        from plone.app.layout.viewlets.common import ViewletBase as Base
        self.assertTrue(issubclass(LinkToOrderViewlet, Base))
        from collective.base.interfaces import IViewlet as Base
        self.assertTrue(issubclass(ILinkToOrderViewlet, Base))

    def test_verifyObject(self):
        from zope.interface.verify import verifyObject
        instance = self.create_viewlet(LinkToOrderViewlet)
        self.assertTrue(verifyObject(ILinkToOrderViewlet, instance))

    @mock.patch('slt.theme.browser.viewlet.getToolByName')
    def test_order_url(self, getToolByName):
        view = mock.Mock()
        view.order_id = 2
        getToolByName().getHomeUrl.return_value = 'HOME_URL'
        instance = self.create_viewlet(LinkToOrderViewlet, view=view)
        self.assertEqual(instance.order_url(), 'HOME_URL?order_number=2')
