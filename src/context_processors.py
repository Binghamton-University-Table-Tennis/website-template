from .models import Images
from .models import OrganizationInformation
from .models import SocialMedia
from .models import ColorScheme

def getBackgroundImage(request):

    photoList = Images.objects.all().filter(Page = Images.BACKGROUND)

    if len(photoList) >= 1:
    	return {'backgroundImage': photoList[0]}
    else:
    	return {}

def getOrganizationInformation(request):

    organizationList = OrganizationInformation.objects.all()

    if len(organizationList) >= 1:
    	return {'organization': organizationList[0]}
    else:
    	return {}

def getSocialMedia(request):

    socialMediaList = SocialMedia.objects.all()

    if len(socialMediaList) >= 1:
    	return {'socialMediaList': socialMediaList}
    else:
    	return {}

def getColorScheme(request):

    colorList = ColorScheme.objects.all()

    if len(colorList) >= 1:
    	return {'headerColor': colorList[0].HeaderColor, 'headerTextColor': colorList[0].HeaderTextColor, 'bodyTextColor': colorList[0].BodyTextColor, 'bodyLinkColor': colorList[0].BodyLinkColor}
    else:
    	return {}