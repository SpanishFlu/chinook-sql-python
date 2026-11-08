# Phase 1: Variables and typecasting
# These are fictional practice values, not database results.

store_name = "Chinook"
database_filename = "Chinook_Sqlite.sqlite"

# Numbers initially stored as text
top_tracks_text = "10"
track_price_text = "0.99"
quantity_text = "3"

# Convert text to numeric types
top_tracks_limit = int(top_tracks_text)
track_price = float(track_price_text)
quantity = int(quantity_text)

print("Store:", store_name)
print("Database:", database_filename)
print("Number of top tracks:", top_tracks_limit)

print("Original quantity type:", type(quantity_text))
print("Converted quantity type:", type(quantity))

total_price = track_price * float(quantity)
print(f"Total price is {total_price:.2f}")
top_tracks_label = str(top_tracks_limit)
print("Top tracks label ", top_tracks_label, type(top_tracks_label))