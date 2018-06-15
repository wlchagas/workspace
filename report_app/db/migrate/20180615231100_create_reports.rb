class CreateReports < ActiveRecord::Migration[5.2]
  def change
    create_table :reports do |t|
      t.string :name
      t.date :date
      t.string :unit

      t.timestamps
    end
  end
end
