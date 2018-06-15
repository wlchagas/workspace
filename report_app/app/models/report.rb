class Report < ApplicationRecord
    has_one :category, inverse_of: :report
    accepts_nested_attributes_for :category, reject_if: :all_blank, allow_destroy: true
end
