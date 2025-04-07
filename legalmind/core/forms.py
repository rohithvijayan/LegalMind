from django import forms
from .models import LegalDocument

class WillForm(forms.ModelForm):
    class Meta:
        model = LegalDocument
        fields = ['name', 'father_name', 'age', 'address', 'executor_name', 'wife_name', 'child_name_1', 'child_name_2', 'flat_no', 'flat_address', 'date', 'month', 'year', 'time']

class LicenseForm(forms.ModelForm):
    class Meta:
        model = LegalDocument
        fields = ['name', 'father_name', 'address', 'date']

class LoanAgreementForm(forms.ModelForm):
    class Meta:
        model = LegalDocument
        fields = ['lender_name', 'borrower_name', 'time', 'loan_amount', 'amount_in_words','loan_period', 'commencement_date', 'termination_date', 'day', 'month', 'year']

class DeedOfHypothecationForm(forms.ModelForm):
    class Meta:
        model = LegalDocument
        fields = ['place', 'day', 'month', 'creditor_name', 'creditor_father_name', 'creditor_age', 'creditor_address', 'borrower_name', 'borrower_father_name', 'borrower_age', 'borrower_address', 'asset_name', 'asset_value', 'manufacturer', 'manufacturer_address', 'advance_payment', 'loan_amount', 'loan_repayment_months', 'start_date', 'interest_rate', 'monthly_payment', 'number_of_missed_installments', 'arbitration_venue']

class BailBondForm(forms.ModelForm):
    class Meta:
        model = LegalDocument
        fields = ['accused_name', 'accused_address', 'name_of_issuing_court', 'offense', 'name_of_appearing_court', 'appearing_day', 'appearing_month', 'appearing_year', 'bail_amount', 'present_day', 'present_month', 'present_year', 'surety_name', 'surety_address', 'name_of_surety_court', 'name_of_trial_court', 'trial_day', 'trial_month', 'trial_year', 'surety_bail_amount']

class ContractBondForm(forms.ModelForm):
    class Meta:
        model = LegalDocument
        fields = ['obligor_name', 'obligor_address', 'obligee_name', 'sum_to_pay', 'plot_address', 'bond_amount', 'present_day', 'present_month', 'present_year']

class SimpleMoneyBondForm(forms.ModelForm):
    class Meta:
        model = LegalDocument
        fields = ['borrower_name', 'borrower_father_name', 'borrower_address', 'lender_name', 'lender_father_name', 'lender_address', 'sum_to_pay', 'sum_in_words', 'object_of_purchase', 'repayment_amount', 'interest_percent', 'date']

class EmployeeBondForm(forms.ModelForm):
    class Meta:
        model = LegalDocument
        fields = ['employee_name', 'employee_address', 'employee_qualification', 'employer_name', 'compensation_amount', 'type_of_product', 'specific_product', 'trade_secret_details', 'penalty_amount', 'restricted_location', 'non_compete_duration']

class MortgageDeedForm(forms.ModelForm):
    class Meta:
        model = LegalDocument
        fields = ['place_of_execution', 'date', 'mortgagor_name', 'mortgagor_father_name', 'mortgagor_address', 'mortgagee_name', 'mortgagee_father_name', 'mortgagee_address', 'property_number', 'property_location', 'loan_amount', 'consideration_amount', 'payment_due_date', 'repayment_amount', 'interest_percent', 'first_installment_date', 'subsequent_installment_payment_day', 'mortgage_property_number', 'mortgage_property_location']
        
class RentAgreementForm(forms.ModelForm):
    class Meta:
        model = LegalDocument
        fields = ['place_of_execution', 'date', 'lessor_name', 'lessor_address', 'lessee_name', 'lessee_address', 'lease_duration_years', 'property_location', 'lease_start_date', 'monthly_rent_amount', 'first_rent_payment_date', 'interest_percent_on_late_payment', 'municipal_and_other_taxes_amount', 'number_of_months_for_default', 'number_of_months_for_dispute_resolution', 'witness_1_name', 'witness_2_name']

class SaleAgreementForm(forms.ModelForm):
    class Meta:
        model = LegalDocument
        fields = ['date', 'seller_name', 'seller_father_name', 'seller_address', 'purchaser_name', 'purchaser_father_name', 'purchaser_age', 'purchaser_address', 'previous_owner_name', 'date_of_previous_sale', 'purpose_of_sale', 'sale_consideration_amount', 'advance_payment_amount', 'cheque_number', 'date_of_advance_payment', 'balance_payment_amount', 'witness_1_name', 'witness_2_name']

class BailPetitionForm(forms.ModelForm):
    class Meta:
        model = LegalDocument
        fields = ['high_court_name', 'accused_name', 'fir_number', 'relevant_legal_sections', 'police_station_name']

class DeedOfAdoptionForm(forms.ModelForm):
    class Meta:
        model = LegalDocument
        fields = ['place_of_execution', 'date', 'adoptive_father_name', 'adoptive_father_address', 'natural_mother_name', 'natural_mother_address', 'child_name', 'biological_father_name', 'previous_marriage_date', 'child_birth_date', 'divorce_petition_number', 'divorce_court_name', 'divorce_order_date', 'date_of_adoption_ceremony', 'religious_ceremony_performed', 'witness_1_name', 'witness_2_name']

class LeaveAndLicenseAgreementForm(forms.ModelForm):
    class Meta:
        model = LegalDocument
        fields = ['place_of_execution', 'date', 'licensor_name', 'licensee_name', 'licensee_address', 'property_address', 'survey_number', 'number_of_floors_in_building', 'built_up_area', 'licensed_portion_of_the_building', 'area_for_use', 'purpose_of_use', 'license_duration', 'monthly_rent', 'rent_per_square_foot', 'rent_due_day', 'witness_1_name', 'witness_2_name']

class PartnershipAgreementForm(forms.ModelForm):
    class Meta:
        model = LegalDocument
        fields = ['place_of_execution', 'date', 'partner_1_name', 'partner_1_age', 'partner_1_father_name', 'partner_1_address', 'partner_2_name', 'partner_2_age', 'partner_2_father_name', 'partner_2_address', 'partner_3_name', 'partner_3_age', 'partner_3_father_name', 'partner_3_address', 'partner_4_name', 'partner_4_age', 'partner_4_father_name', 'partner_4_address', 'purpose_of_business', 'business_name', 'business_address', 'previous_partnership_deed_date', 'capital_investment_date', 'working_partner_1', 'working_partner_2', 'working_partner_3', 'remuneration_percentage_1', 'remuneration_percentage_2', 'remuneration_percentage_3', 'partner_1_share_of_profit', 'partner_2_share_of_profit', 'partner_3_share_of_profit', 'partner_4_share_of_profit', 'sleeping_partner_names', 'witness_1_name', 'witness_2_name']

class DeedOfGiftOfImmoveablePropertyForm(forms.ModelForm):
    class Meta:
        model = LegalDocument
        fields = ['place_of_execution', 'date', 'donor_name', 'donor_address', 'donee_name', 'donee_address', 'property_location', 'donor_relationship_to_donee', 'property_market_value', 'witness_1_name', 'witness_2_name']

class MemorandumRecordingFamilySettlementForm(forms.ModelForm):
    class Meta:
        model = LegalDocument
        fields = ['place_of_execution', 'date', 'party_1_name', 'party_1_address', 'party_2_name', 'party_2_address', 'party_3_name', 'party_3_address', 'relationship_between_party_1_and_party_2', 'dispute_subject', 'deceased_person_name', 'liabilities_amount', 'expenses_amount', 'bank_name', 'execution_date', 'witness_1_name', 'witness_2_name']

class PartitionDeedForm(forms.ModelForm):
    class Meta:
        model = LegalDocument
        fields = ['place_of_execution', 'date', 'first_party_name', 'first_party_father_name', 'first_party_address', 'second_party_name', 'second_party_father_name', 'second_party_address', 'third_party_name', 'third_party_father_name', 'third_party_address', 'karta_name', 'family_name', 'wife_name', 'other_member_name', 'phone_number_1', 'phone_number_2', 'shares_count_1', 'company_name_1', 'bank_balance_1', 'bank_name_1', 'branch_name_1', 'date_of_agreement', 'shares_value_1', 'company_name_2', 'shares_value_2', 'total_value', 'recipient_name', 'net_capital_of_family', 'bank_balance_2', 'donated_amount', 'charitable_trust_name', 'partition_date', 'allocated_phone_number', 'witness_1_name', 'witness_2_name']

class SeparationAgreementForm(forms.ModelForm):
    class Meta:
        model = LegalDocument
        fields = ['city', 'date', 'husband_name', 'husband_father_name', 'husband_residence_address', 'wife_name', 'maintenance_amount_from_husband', 'first_child_name', 'second_child_name', 'first_child_age', 'second_child_age', 'husband_visiting_time_start', 'husband_visiting_time_end', 'witness_1_name', 'witness_2_name']

class GeneralPowerOfAttorneyForm(forms.ModelForm):
    class Meta:
        model = LegalDocument
        fields = ['principal_name', 'principal_address', 'attorney_name', 'attorney_address', 'execution_date', 'place_of_execution', 'witness_name']

class IrrevocablePowerOfAttorney(forms.ModelForm):
    class Meta:
        model = LegalDocument
        fields = ['company_name', 'company_registered_office', 'authorized_person_name', 'principal_place_of_business', 'partner_name', 'loan_amount', 'loan_amount_in_words', 'signatory_name', 'execution_date', 'witness_name']

class RevocationOfThePowerOfAttorneyForm(forms.ModelForm):
    class Meta:
        model = LegalDocument
        fields = ['principal_name', 'father_name', 'principal_address', 'attorney_name', 'attorney_father_name', 'attorney_address', 'power_of_attorney_date', 'execution_date']

class GiftDeedForm(forms.ModelForm):
    class Meta:
        model = LegalDocument
        fields = ['execution_date', 'donor_name', 'donor_age', 'donor_address', 'donor_age', 'donee_name', 'donee_age', 'donee_address', 'gift_amount', 'cheque_number', 'bank_name', 'branch_name', 'cheque_date', 'witness_1_name', 'witness_1_address', 'witness_2_name', 'witness_2_address']

class AgreementLicenseBetweenTrademarkOwnerAndManufacturer(forms.ModelForm):
    class Meta:
        model = LegalDocument
        fields = ['date_of_agreement', 'licensor_company_name', 'licensor_address', 'licensee_name', 'licensee_business', 'goods_description', 'licensee_factory_address', 'goods_price_per_item', 'monthly_quantity_of_goods_to_be_supplied_by_licensee', 'licensor_business_address', 'royalty_percentage', 'agreement_duration', 'licensor_witness_name', 'licensee_witness_name']

class AffidavitAndIndemnityForm(forms.ModelForm):
    class Meta:
        model = LegalDocument
        fields = ['affiant_name', 'beneficiary_name', 'affiant_age', 'employer_name', 'premises_address', 'name_of_licensor_of_premise', 'leave_and_license_agreement_date', 'authority_name', 'indemnified_party', 'name_of_the_entity_suffering_damages_due_to_affiants_non_compliance', 'authority_name', 'legal_advising_party', 'date']

class AgreementBetweenIndependentContractorAndServiceProvider(forms.ModelForm):
    class Meta:
        model = LegalDocument
        fields = ['date', 'company_name', 'company_address', 'independent_contractor_name', 'termination_notice_period', 'governing_state', 'name_of_contractor', 'the_work_or_service_to_be_performed', 'maximum_compensation_amount', 'lump_sum_amount', 'payment_schedule']

class NDAForm(forms.ModelForm):
    class Meta:
        model = LegalDocument
        fields = ['party_1_name', 'party_1_address', 'party_2_name', 'party_2_address', 'subject_of_first_party_information', 'subject_of_second_party_information', 'oral_disclosure_notice_days', 'confidentiality_notice_days', 'confidentiality_period', 'export_country', 'agreement_term', 'governing_law_location', 'party_1_designation', 'party_2_designation']