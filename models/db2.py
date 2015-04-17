db.define_table('newspaper',
                Field('choice_of_newspaper', requires=IS_IN_SET(['The Times of India', 'The Hindu', 'The White Fur'])),
                Field('subscription_type', requires=IS_IN_SET(['Yearly', 'Monthly'])),
                Field('subscriber', 'reference auth_user', writable=False, readable=False))
