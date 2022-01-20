from behave import given, when, then


@given(u'demo page is open')
def step_impl(context):
    print(context.feature.name)
    print(context.scenario.name)
    print("This is given")


@when(u'user enters full name as {full_name}')
def step_impl(context, full_name):
    #print(type(full_name))
    print("This is when full name {}".format(full_name))


@when(u'user enters contact number as {contact_number}')
def step_impl(context, contact_number):
    #print(type(contact_number))
    print("This is when contact number {}".format(contact_number))


@when(u'user enters email address as {email}')
def step_impl(context,email):
    print("This is when email, {}".format(email))


@when(u'user click on button {button}')
def step_impl(context, button):
    print("This is when click {} button".format(button))


@then(u'validation message should be displayed')
def step_impl(context):
    print("This is then validation")