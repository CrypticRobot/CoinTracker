from wtforms import Form, StringField, validators, HiddenField, PasswordField, IntegerField

class APIPrice(Form):
    target = StringField(
        u'target',
        [validators.InputRequired(), validators.Length(min=3, max=5)]
    )

    against = StringField(
        u'against',
        [validators.InputRequired(), validators.Length(min=3, max=5)]
    )

    before = IntegerField(
        u'before',
        [validators.Optional(), validators.NumberRange(min=0, max=253402300799)]
    )

    after = IntegerField(
        u'after',
        [validators.Optional(), validators.NumberRange(min=0, max=253402300799)]
    )

    time_elapse = IntegerField(
        u'time_elapse',
        [validators.Optional(), validators.NumberRange(min=0, max=30)],
    )

    time_unit = StringField(
        u'time_unit',
        [validators.Optional(), validators.AnyOf(['min', 'hour', 'day', 'week'])],
    )

    limit = IntegerField(
        u'limit',
        [validators.Optional(), validators.NumberRange(min=0, max=300)],
    )

class APISingle(Form):
    target = StringField(
        u'target',
        [validators.InputRequired(), validators.Length(min=3, max=5)]
    )

    against = StringField(
        u'against',
        [validators.InputRequired(), validators.Length(min=3, max=5)]
    )

    time_elapse = IntegerField(
        u'time_elapse',
        [validators.Optional(), validators.NumberRange(min=0, max=30)],
    )

    time_unit = StringField(
        u'time_unit',
        [validators.Optional(), validators.AnyOf(['min', 'hour', 'day', 'week'])],
    )

class DemoPage(Form):
    target = StringField(
        u'target',
        [validators.InputRequired(), validators.Length(min=3, max=5)]
    )

    against = StringField(
        u'against',
        [validators.InputRequired(), validators.Length(min=3, max=5)]
    )
    
    time_unit = StringField(
        u'time_unit',
        [validators.Optional(), validators.AnyOf(['min', 'hour', 'day', 'week'])],
    )