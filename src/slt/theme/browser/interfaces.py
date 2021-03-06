from collective.base.interfaces import IBaseFormView
from collective.base.interfaces import IViewlet
from collective.cart.shopping.browser.interfaces import IBillingAndShippingBillingAddressViewlet as IBaseBillingAndShippingBillingAddressViewlet
from collective.cart.shopping.browser.interfaces import ICollectiveCartShoppingLayer
from collective.cart.shopping.browser.interfaces import IOrderListingViewletManager as IBaseOrderListingViewletManager
from sll.basetheme.browser.interfaces import INavigationRootView
from zope.viewlet.interfaces import IViewletManager


# Browser layer

class ISltThemeLayer(ICollectiveCartShoppingLayer):
    """Marker interface for browserlayer."""


# Viewlet manager

class IBaseViewViewletManager(IViewletManager):
    """Viewlet manager interface for base view"""


class IOrderListingViewletManager(IBaseOrderListingViewletManager):
    """Viewlet manager interface for OrderListingViewletManager"""


# View

class IShopView(IBaseFormView, INavigationRootView):
    """View interface for ShopView"""


class IMembersView(IBaseFormView, INavigationRootView):
    """View interface for @@members"""

    def all_members():
        """Returns list of all the members

        :rtype: list
        """

    def direct_marketing_allowers():
        """Returns list of memebers who allow direct marketing

        :rtype: list
        """

    def table_headers():
        """Returns headers for table

        :rtype: tuple
        """


class IAddressListingView(IBaseFormView):
    """View interface for AddressListingView"""


class IOrderListingView(IBaseFormView):
    """View interface for OrderListingView"""


# Viewlet

class ILinkToOrderViewlet(IViewlet):
    """Viewlet interface for LinkToOrderViewlet"""

    def order_url():
        """Returns URL for order

        :rtype: str
        """


class IShopArticleListingViewlet(IViewlet):
    """Viewlet interface for ShopArticleListingViewlet"""

    def articles():
        """Returns list of dictionary of articles

        :rtype: list
        """


class IMembersExportViewlet(IViewlet):
    """Viewlet interface for MembersExportViewlet"""


class IAddAddressViewlet(IViewlet):
    """Viewlet interface for AddAddressViewlet"""


class IAddressListingViewlet(IViewlet):
    """Viewlet interface for AddressListingViewlet"""

    def addresses():
        """Returns list of dictionary of addresses

        :rtype: list
        """

    def class_collapsible():
        """Returns class for styling

        :rtype: str
        """


class IOrderListingViewlet(IViewlet):
    """View interface for OrderListingViewlet"""

    def orders():
        """Returns list of dictionary of orders

        :rtype: list
        """

    def class_collapsible():
        """Returns styling values

        :rtype: str
        """


class IBillingAndShippingBillingAddressViewlet(IBaseBillingAndShippingBillingAddressViewlet):
    """Viewlet interface for BillingAndShippingBillingAddressViewlet"""

    def today():
        """Today"""

    def localized_today():
        """Localized today

        :rtype: unicode
        """

    def birth_date():
        """Return birth date

        :rtype: str
        """

    def localized_birth_date():
        """Return localized birth date

        :rtype: unicode
        """

    def registration_number():
        """Return registration number

        :rtype: str
        """

    def use_verkkolasku():
        """Return True if use verkkolasku otherwise False

        :rtype: boolean
        """

    def use_verkkolasku_checked():
        """Return checked if use verkkolasku otherwise empty string

        :rtype: str
        """

    def verkkolasku_operator():
        """Return verkkolasku operator

        :rtype: str
        """

    def verkkolasku_account():
        """Return verkkolasku intermediator account

        :rtype: int
        """


class IOrderConfirmationRegistrationNumberViewlet(IViewlet):
    """Viewlet interface for OrderConfirmationRegistrationNumberViewlet"""

    def registration_number():
        """Returns registration number

        :rtype: str
        """


class IOrderListingRegistrationNumberViewlet(IViewlet):
    """Viewlet interface for OrderListingRegistrationNumberViewlet"""


class IOrderListingBirthDateViewlet(IViewlet):
    """Viewlet interface for OrderListingBirthDateViewlet"""


class IOrderListingVerkkolaskuViewlet(IViewlet):
    """Viewlet interface for OrderListingVerkkolaskuViewlet"""
