# Constants
MAX_QUALITY = 50
PAST_SELL_BY_DATE_DECAY = 2
BEFORE_SELL_BY_DATE_DECAY = 1
NORMAL = 1
TWICE = 2
LAST_MINUTE = 10 # days
LAST_LAST_MINUTE = 5 # days
LAST_MINUTE_PREMIUM = 2
LAST_LAST_MINUTE_PREMIUM = 3

ItemFactorySingleton = (name, sellBy , quality) ->
  @name = name
  @sellBy = sellBy
  @quality = quality

items = [] 
items.push new ItemFactorySingleton("+5 Dexterity Vest", 10, 20) # Great for Rouges
items.push new ItemFactorySingleton("Aged Brie", 2, 0) # Stinky
items.push new ItemFactorySingleton("Elixir of the Mongoose", 5, 7) # Mongoose vs. Cobra: FIGHT!
items.push new ItemFactorySingleton("Sulfuras, Hand of Ragnaros", 0, 80) # Legendary
items.push new ItemFactorySingleton("Backstage passes to a TAFKAL80ETC concert", 15, 20) # The Artist Formerly Known As Level 80 Tauren Chieftains
items.push new ItemFactorySingleton("Conjured Mana Cake", 3, 6) # TODO: add conjured item logic to update quality function

reduceQuality = (quality, amount = 1) ->
  if quality > 0
    quality - amount
  else 
    0

increaseQuality = (quality, amount = 1) ->
  if (quality + amount) < MAX_QUALITY
    quality + amount
  else
    MAX_QUALITY

updateAgedBrie = (item) ->
  item.sellBy--
  item.quality = increaseQuality item.quality

updateBackstagePasses = (item) ->
  item.sellBy--        
  if item.sellBy < 0
    item.quality = 0          
  else
    if item.sellBy > LAST_MINUTE
      item.quality = increaseQuality item.quality
    if LAST_LAST_MINUTE < item.sellBy <= LAST_MINUTE
      item.quality = increaseQuality item.quality, LAST_MINUTE_PREMIUM
    if item.sellBy <= LAST_LAST_MINUTE
      item.quality = increaseQuality item.quality, LAST_LAST_MINUTE_PREMIUM

reduceByAmount = (sellBy, conjured) ->
  multiplier = if conjured then TWICE else NORMAL
  if sellBy < 0 
    PAST_SELL_BY_DATE_DECAY * multiplier
  else 
    BEFORE_SELL_BY_DATE_DECAY * multiplier

updateGenericItem = (item, conjured = false) ->
  item.sellBy--
  item.quality = item.quality - reduceByAmount(item.sellBy, conjured)

updateItem = (item) ->
  switch item.name 
    when "Aged Brie" 
      updateAgedBrie item
    when "Sulfuras, Hand of Ragnaros"
      break # sufuras never changes quality and never needs to be sold
    when "Backstage passes to a TAFKAL80ETC concert"
      updateBackstagePasses item
    when "Conjured Mana Cake"
      updateGenericItem item, true
    else  # everything else
      updateGenericItem item

update_quality = (items) ->
  for item in items
    updateItem item

exports.updateQuality = update_quality
exports.items = items
exports.reduceByAmount = reduceByAmount

