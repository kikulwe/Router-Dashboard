
from django.shortcuts import render
from script import TplinkDeviceScanner

def router_dashboard(request):
    # Replace 'your_router_host', 'your_router_username', and 'your_router_password'
    # with the actual credentials for your TP-Link router.
    tplink_scanner = TplinkDeviceScanner('your_router_host', 'your_router_username', 'your_router_password')

    connected_devices = tplink_scanner.scan_devices()

    context = {
        'connected_devices': connected_devices,
        # Add other context data for your dashboard here...
    }

    return render(request, 'router_dashboard.html', context)
