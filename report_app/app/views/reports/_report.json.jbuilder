json.extract! report, :id, :name, :date, :unit, :created_at, :updated_at
json.url report_url(report, format: :json)
