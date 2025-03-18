from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from subscriptions.models import Subscription, Addon, UserSubscription, Coupon


@csrf_exempt
def success_response(request):
    redirect = False
    try:
        s_id = request.GET.get('s_id')
        txn_id = request.GET.get('txn_id')
        amount = request.GET.get('amount')
        product_info = request.GET.get('product_info')
        first_name = request.GET.get('first_name')
        email = request.GET.get('email')
        phone = request.GET.get('phone')
        coupon = request.GET.get('coupon')
        add_ons = list(request.GET.get('add_ons', []))
        if '[' in add_ons:
            add_ons.remove('[')
        if ']' in add_ons:
            add_ons.remove(']')
        if ',' in add_ons:
            add_ons.remove(',')
        subscription = Subscription.objects.filter(id=s_id).first()
        addons = Addon.objects.filter(id__in=add_ons)

        total_messages = subscription.messages + sum(addon.messages for addon in addons)
        total_calls = subscription.calls + sum(addon.calls for addon in addons)
        user_subscription = UserSubscription.objects.create(subscription=subscription, txn_id=txn_id, amount=amount, product_info=product_info, firstname=first_name, email=email, phone=phone, coupon=coupon, status="Success")
        user_subscription.messages = total_messages
        user_subscription.calls = total_calls
        if addons:
            user_subscription.addons.set(addons)
        user_subscription.save()

        couponObj = Coupon.objects.filter(code=coupon).first()
        if couponObj:
            couponObj.usage_count += 1
            couponObj.save()
        redirect = True
    except Exception as err:
        print(err, '+++++++++++++')
    return render(request, 'success.html', {'redirect': redirect})

@csrf_exempt
def failure_response(request):
    return render(request, 'failure.html')
