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

update_quality = (items) ->
  index = 0 
  MAX_QUALITY = 50

  for item in items
    switch item.name 
      when "Aged Brie" 
        item.sellBy--
        if item.quality < MAX_QUALITY
          item.quality++  
      when "Sulfuras, Hand of Ragnaros"
        break # sufuras never changes quality and never needs to be sold
      when "Backstage passes to a TAFKAL80ETC concert"
        item.sellBy--        
        if item.sellBy > 10
          item.quality++
        if 5 < item.sellBy <= 10
          item.quality = item.quality + 2 
        if item.sellBy <= 5
          item.quality = item.quality + 3
        if item.sellBy < 0
          item.quality = 0          
        if item.quality > MAX_QUALITY
          item.quality = MAX_QUALITY
      else  # everything else
        item.sellBy--
        if item.sellBy < 0
          item.quality = 0
        else
          if item.quality > 0
            item.quality--

exports.updateQuality = update_quality
exports.items = items
