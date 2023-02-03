from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from apps.home.models import Campaign, Faucet, WashroomGroups


@login_required(login_url="/login/")
def get_washrooms(request, venue=None):
    if request.method == 'GET':
        washroom_options = []
        if venue:
            washrooms = WashroomGroups.objects.filter(washrooms__venues=venue)
            for w in washrooms:
                washroom_options.append({
                    'id': w.id,
                    'name': w.get_washrooms()
                })

        data = {
            'washroom_options': washroom_options,
        }
        return JsonResponse(data)


def api_login(request):
    data = {}
    if request.method == 'GET':
        token = r"qEukfbNJ70Waitk2AvycmtfP?xel-9/pwps6iRSQ"
        mac = request.GET.get('mac', None)

        if mac:
            faucet, created = Faucet.objects.get_or_create(mac=str(mac))

            if created:
                faucet.name = "Faucet created from API"

            faucet.status = "ONLINE"
            faucet.save()
        else:
            mac = "please, use a correct MAC address"
            token = None

        data = {
            'mac': mac,
            'token': token
        }

    return JsonResponse(data)


def api_get_date(request):
    data = {}
    if request.method == 'GET':

        data = {
            'command': "SetDate",
            'message': "2023-01-01"
        }

    return JsonResponse(data)


def api_get_playlist(request):
    data = {}
    if request.method == 'GET':
        all_data = []
        message = ""
        mac = request.GET.get('mac', None)

        if mac:
            faucet, created = Faucet.objects.get_or_create(mac=str(mac))

            if created:
                faucet.name = "Faucet created from API"
                message = "The faucet has recently created"

            faucet.status = "ONLINE"
            faucet.save()

            if not created:
                if faucet.washroom:
                    try:
                        campaigns = Campaign.objects.filter(
                            washroom_groups=faucet.washroom.washroom_groups)

                        for campaign in campaigns.all():
                            videos = campaign.get_media_urls()
                            dates = {
                                "begin": str(campaign.start_date),
                                "end": str(campaign.end_date)
                            }

                            data = {
                                "command": "SetPlay",
                                "message": message,
                                "videos": videos,
                                "date": dates,
                            }
                            all_data.append(data)

                        return JsonResponse(all_data, safe=False)

                    except Campaign.DoesNotExist:
                        message = "NO DATA"
                else:
                    message = "This faucet does not have any Washroom linked"
        else:
            message = "Please, use a correct MAC address"

        data = {
            "command": "SetPlay",
            "message": message,
            "videos": [],
            "date": "",
        }

    return JsonResponse(data)
