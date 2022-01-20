

def before_all(context):
    print("Before All")


def before_feature(context, feature):
    print("Before feature")


def before_scenario(conext, scenaro):
    print("Before scenario")


def before_step(context, step):
    print("Before step")


def after_step(contex,step):
    print("After step")
    print(step.status.name)


def after_scenario(context, scenario):
    print("After scenario")
    print(scenario.status.name)


def after_feature(context,feature):
    print("After feature")
    print(feature.status.name)


def after_all(context):
    print("After all")
