from django.db import models

class LegalDocument(models.Model):
    DOCUMENT_CHOICES = [
        ('will', 'Simple Will'),
        ('license', 'License Agreement'),
        ('loan_agreement', 'Loan Agreement'),
        ('deed_of_hypothecation', 'Deed Of Hypothecation'),
        ('contract_bond', 'Contract Bond'),
        ('simple_money_bond', 'Simple Money Bond'),
        ('employee_bond_for_non_compete', 'Employee Bond for Non-Compete'),
        ('simple_mortgage_deed', 'Simple Mortgage Deed'),
        ('rent_agreement', 'Rent Agreement (For a term of years)'),
        ('sale_agreement', 'Agreement For Sale'),
        ('anticipatory_bail_petition_format', 'Anticipatory Bail Petition Format'),
        ('deed_of_adoption', 'Deed Of Adoption'),
        ('leave_and_license_agreement', 'Leave and License Agreement'),

    ]
    document_type = models.CharField(max_length=255, choices=DOCUMENT_CHOICES)
    name = models.CharField(max_length=255)
    father_name = models.CharField(max_length=255)
    age = models.IntegerField(blank=True, null=True)
    address = models.TextField()
    executor_name = models.CharField(max_length=255, blank=True, null=True)
    wife_name = models.CharField(max_length=255, blank=True, null=True)
    child_name_1 = models.CharField(max_length=255, blank=True, null=True)
    child_name_2 = models.CharField(max_length=255, blank=True, null=True)
    flat_no = models.CharField(max_length=50, blank=True, null=True)
    flat_address = models.TextField(blank=True, null=True)
    date = models.CharField(max_length=50)
    month = models.CharField(max_length=50, blank=True, null=True)
    year = models.CharField(max_length=50, blank=True, null=True)
    time = models.CharField(max_length=50, blank=True, null=True)
    
    #loan_agreement
    lender_name = models.CharField(max_length=255, blank=True, null=True)
    borrower_name = models.CharField(max_length=255, blank=True, null=True)
    loan_amount = models.CharField(max_length=50, blank=True, null=True)
    amount_in_words = models.CharField(max_length=255, blank=True, null=True)
    loan_period = models.CharField(max_length=50, blank=True, null=True)
    commencement_date = models.CharField(max_length=50, blank=True, null=True)
    termination_date = models.CharField(max_length=50, blank=True, null=True)
    day = models.IntegerField(blank=True, null=True)

    #deed of hypothecation
    place = models.CharField(max_length=255, blank=True, null=True)
    
    month = models.CharField(max_length=255, blank=True, null=True)
    creditor_name = models.CharField(max_length=255, blank=True, null=True)
    creditor_father_name = models.CharField(max_length=255, blank=True, null=True)
    creditor_age = models.IntegerField(blank=True, null=True)
    creditor_address = models.CharField(max_length=255, blank=True, null=True)
    #borrower_name = models.CharField(max_length=255, blank=True, null=True)
    borrower_father_name = models.CharField(max_length=255, blank=True, null=True)
    borrower_age = models.IntegerField(blank=True, null=True)
    borrower_address = models.CharField(max_length=255, blank=True, null=True)
    asset_name = models.CharField(max_length=255, blank=True, null=True)
    asset_value = models.IntegerField(blank=True, null=True)
    manufacturer = models.CharField(max_length=255, blank=True, null=True)
    manufacturer_address = models.CharField(max_length=255, blank=True, null=True)
    advance_payment = models.IntegerField(blank=True, null=True)
    #loan_amount = models.IntegerField(blank=True, null=True)
    loan_repayment_months = models.IntegerField(blank=True, null=True)
    start_date = models.CharField(max_length=50, blank=True, null=True)
    interest_rate = models.IntegerField(blank=True, null=True)
    monthly_payment = models.IntegerField(blank=True, null=True)
    number_of_missed_installments = models.IntegerField(blank=True, null=True)
    arbitration_venue = models.CharField(max_length=255, blank=True, null=True)

    #bond and bail bond
    accused_name = models.CharField(max_length=255, blank=True, null=True)
    accused_address = models.CharField(max_length=255, blank=True, null=True)
    name_of_issuing_court = models.CharField(max_length=255, blank=True, null=True)
    offense = models.CharField(max_length=255, blank=True, null=True)
    name_of_appearing_court = models.CharField(max_length=255, blank=True, null=True)
    appearing_day = models.IntegerField(blank=True, null=True)
    appearing_month = models.CharField(max_length=255, blank=True, null=True)
    appearing_year = models.IntegerField(blank=True, null=True)
    bail_amount = models.FloatField(blank=True, null=True)
    present_day = models.IntegerField(blank=True, null=True)
    present_month = models.CharField(max_length=255, blank=True, null=True)
    present_year = models.IntegerField(blank=True, null=True)
    surety_name = models.CharField(max_length=255, blank=True, null=True)
    surety_address = models.CharField(max_length=255, blank=True, null=True)
    name_of_surety_court = models.CharField(max_length=255, blank=True, null=True)
    name_of_trial_court = models.CharField(max_length=255, blank=True, null=True)
    trial_day = models.IntegerField(blank=True, null=True)
    trial_month = models.CharField(max_length=255, blank=True, null=True)
    trial_year = models.IntegerField(blank=True, null=True)
    surety_bail_amount = models.IntegerField(blank=True, null=True)

    #contract bond
    obligor_name = models.CharField(max_length=255, blank=True, null=True)
    obligor_address = models.CharField(max_length=255, blank=True, null=True)
    obligee_name = models.CharField(max_length=255, blank=True, null=True)
    sum_to_pay = models.IntegerField(blank=True, null=True)
    plot_address = models.CharField(max_length=255, blank=True, null=True)
    bond_amount = models.IntegerField(blank=True, null=True)
    present_day = models.IntegerField(blank=True, null=True)
    present_month = models.CharField(max_length=255, blank=True, null=True)
    present_year = models.IntegerField(blank=True,null=True)

    #simplemoneybond
    lender_father_name = models.CharField(max_length=255, blank=True, null=True)
    lender_address = models.CharField(max_length=255, blank=True, null=True)
    sum_in_words = models.IntegerField(blank=True, null=True)
    object_of_purchase = models.CharField(max_length=255, blank=True, null=True)
    repayment_amount = models.IntegerField(blank=True, null=True)
    interest_percent = models.IntegerField(blank=True, null=True)

    #employee bond for non-compete
    employee_name = models.CharField(max_length=255, blank=True, null=True)
    employee_address = models.CharField(max_length=255, blank=True, null=True)
    employee_qualification = models.CharField(max_length=255, blank=True, null=True)
    employer_name = models.CharField(max_length=255, blank=True, null=True)
    compensation_amount = models.FloatField(blank=True, null=True)
    type_of_product = models.CharField(max_length=255, blank=True, null=True)
    specific_product = models.CharField(max_length=255, blank=True, null=True)
    trade_secret_details = models.CharField(max_length=255, blank=True, null=True)
    penalty_amount = models.FloatField(blank=True, null=True)
    restricted_location = models.CharField(max_length=255, blank=True, null=True)
    non_compete_duration = models.CharField(max_length=255, blank=True, null=True)

    #simple mortgage deed
    place_of_execution = models.CharField(max_length=255, blank=True, null=True)
    mortgagor_name = models.CharField(max_length=255, blank=True, null=True)
    mortgagor_father_name = models.CharField(max_length=255, blank=True, null=True)
    mortgagor_address = models.CharField(max_length=255, blank=True, null=True)
    mortgagee_name = models.CharField(max_length=255, blank=True, null=True)
    mortgagee_father_name = models.CharField(max_length=255, blank=True, null=True)
    mortgagee_address = models.CharField(max_length=255, blank=True, null=True)
    property_number = models.CharField(max_length=255, blank=True, null=True)
    property_location = models.CharField(max_length=255, blank=True, null=True)
    loan_amount = models.FloatField(blank=True, null=True)
    consideration_amount = models.FloatField(blank=True, null=True)
    payment_due_date = models.CharField(max_length=255, blank=True, null=True)
    repayment_amount = models.FloatField(blank=True, null=True)
    interest_percent = models.IntegerField(blank=True, null=True)
    first_installment_date = models.CharField(max_length=255, blank=True, null=True)
    subsequent_installment_payment_day = models.IntegerField(blank=True, null=True)
    mortgage_property_number = models.IntegerField(blank=True, null=True)
    mortgage_property_location = models.CharField(max_length=255, blank=True, null=True)

    #rentagreement
    place_of_execution = models.CharField(max_length=255, blank=True, null=True)
    lessor_name = models.CharField(max_length=255, blank=True, null=True)
    lessor_address = models.CharField(max_length=255, blank=True, null=True)
    lessee_name = models.CharField(max_length=255, blank=True, null=True)
    lessee_address = models.CharField(max_length=255, blank=True, null=True)
    lease_duration_years = models.IntegerField(blank=True, null=True)
    lease_start_date = models.CharField(max_length=255, blank=True, null=True)
    monthly_rent_amount = models.FloatField(blank=True, null=True)
    first_rent_payment_date = models.CharField(max_length=255, blank=True, null=True)
    interest_percent_on_late_payment = models.FloatField(blank=True, null=True)
    municipal_and_other_taxes_amount = models.FloatField(blank=True, null=True)
    number_of_months_for_default = models.IntegerField(blank=True, null=True)
    number_of_months_for_dispute_resolution = models.IntegerField(blank=True, null=True)
    witness_1_name = models.CharField(max_length=255, blank=True, null=True)
    witness_2_name = models.CharField(max_length=255, blank=True, null=True)

    #saleagreement
    seller_name = models.CharField(max_length=255, blank=True, null=True)
    seller_father_name = models.CharField(max_length=255, blank=True, null=True)
    seller_address = models.CharField(max_length=255, blank=True, null=True)
    purchaser_name = models.CharField(max_length=255, blank=True, null=True)
    purchaser_father_name = models.CharField(max_length=255, blank=True, null=True)
    purchaser_age = models.IntegerField(blank=True, null=True)
    purchaser_address = models.CharField(max_length=255, blank=True, null=True)
    previous_owner_name = models.CharField(max_length=255, blank=True, null=True)
    date_of_previous_sale = models.CharField(max_length=255, blank=True, null=True)
    purpose_of_sale = models.CharField(max_length=255, blank=True, null=True)
    sale_consideration_amount = models.FloatField(blank=True, null=True)
    advance_payment_amount = models.FloatField(blank=True, null=True)
    cheque_number = models.IntegerField(blank=True, null=True)
    date_of_advance_payment = models.CharField(max_length=255, blank=True, null=True)
    balance_payment_amount = models.FloatField(blank=True, null=True)
    
    #anticipatory_bail_petition_format
    high_court_name = models.CharField(max_length=255, blank=True, null=True)
    accused_name = models.CharField(max_length=255, blank=True, null=True)
    fir_number = models.IntegerField(blank=True, null=True)
    relevant_legal_sections = models.CharField(max_length=255, blank=True, null=True)
    police_station_name = models.CharField(max_length=255, blank=True, null=True)

    #deed of adoption
    place_of_execution = models.CharField(max_length=255, blank=True, null=True)
    adoptive_father_name = models.CharField(max_length=255, blank=True, null=True)
    adoptive_father_address = models.CharField(max_length=255, blank=True, null=True)
    natural_mother_name = models.CharField(max_length=255, blank=True, null=True)
    natural_mother_address = models.CharField(max_length=255, blank=True, null=True)
    child_name = models.CharField(max_length=255, blank=True, null=True)
    biological_father_name = models.CharField(max_length=255, blank=True, null=True)
    previous_marriage_date = models.CharField(max_length=255, blank=True, null=True)
    child_birth_date = models.CharField(max_length=255, blank=True, null=True)
    divorce_petition_number = models.CharField(max_length=255, blank=True, null=True)
    divorce_court_name = models.CharField(max_length=255, blank=True, null=True)
    divorce_order_date = models.CharField(max_length=255, blank=True, null=True)
    date_of_adoption_ceremony = models.CharField(max_length=255, blank=True, null=True)
    religious_ceremony_performed = models.CharField(max_length=255, blank=True, null=True)

    #leave and license agreement
    licensor_name = models.CharField(max_length=255, blank=True, null=True)
    licensee_name = models.CharField(max_length=255, blank=True, null=True)
    licensee_address = models.CharField(max_length=255, blank=True, null=True)
    property_address = models.CharField(max_length=255, blank=True, null=True)
    survey_number = models.IntegerField(blank=True, null=True)
    number_of_floors_in_building = models.IntegerField(blank=True, null=True)
    built_up_area = models.CharField(max_length=255, blank=True, null=True)
    licensed_portion_of_the_building = models.CharField(max_length=255, blank=True, null=True)
    area_for_use = models.CharField(max_length=255, blank=True, null=True)
    purpose_of_use = models.CharField(max_length=255, blank=True, null=True)
    license_duration = models.CharField(max_length=255, blank=True, null=True)
    monthly_rent = models.FloatField(blank=True, null=True)
    rent_per_square_foot = models.FloatField(blank=True, null=True)
    rent_due_day = models.CharField(max_length=255, blank=True, null=True)
    

       