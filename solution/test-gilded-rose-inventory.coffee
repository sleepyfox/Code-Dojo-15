should = require('chai').should()
IM = require './InventoryManager'
[items, updateQuality] = [IM.items, IM.updateQuality]

qualityTable = {
  days: [
    {
      items: [
        { name: "+5 Dexterity Vest", sellBy: 10, quality: 20},
        { name: "Aged Brie", sellBy: 2, quality: 0},
        { name: "Elixir of the Mongoose", sellBy: 5, quality: 7},
        { name: "Sulfuras, Hand of Ragnaros", sellBy: 0, quality: 80},
        { name: "Backstage passes to a TAFKAL80ETC concert", sellBy: 15, quality: 20},
        { name: "Conjured Mana Cake", sellBy: 3, quality: 6},
      ]
    }
  ]
}

describe 'Gilded Rose tests', ->
  describe 'test inventory setup', ->
    it 'there should be 6 items in the inventory', ->
      items.should.have.length 6
    
  describe 'After day 1...', ->

    it '+5 Dexterity Vest should have quality 19', ->
      updateQuality items
      items[0].quality.should.equal 19

    it '+5 Dexterity Vest should have 9 days left to sell', ->
      items[0].sellBy.should.equal 9

    it 'Aged Brie should have quality 1', ->
      items[1].quality.should.equal 1

    it 'Aged Brie should have 1 day left to sell', ->
      items[1].sellBy.should.equal 1
    
    it 'Elixir of the Mongoose should have quality 6', ->
      items[2].quality.should.equal 6

    it 'Elixir of the Mongoose should have 4 days left to sell', ->
      items[2].sellBy.should.equal 4

    it 'Sulfuras, Hand of Ragnaros should have quality 80', ->
      items[3].quality.should.equal 80

    it 'Sulfuras, Hand of Ragnaros should have 0 days left to sell', ->
      items[3].sellBy.should.equal 0

    it 'Backstage passes should have quality 20', ->
      items[4].quality.should.equal 21

    it 'Backstage passes should have 14 days left to sell', ->
      items[4].sellBy.should.equal 14

    xit 'Conjured Mana Cake should have quality 4', ->
      items[5].quality.should.equal 4

    it 'Conjured Mana Cake should have 2 days left to sell', ->
      items[5].sellBy.should.equal 2

  describe 'After day 2...', ->
    it '+5 Dexterity Vest should have quality 18', ->
      updateQuality items
      items[0].quality.should.equal 18

    it '+5 Dexterity Vest should have 8 days left to sell', ->
      items[0].sellBy.should.equal 8

    it 'Aged Brie should have quality 2', ->
      items[1].quality.should.equal 2
    
    it 'Aged Brie should have 0 days left to sell', ->
      items[1].sellBy.should.equal 0

    it 'Elixir of the Mongoose should have quality 5', ->
      items[2].quality.should.equal 5

    it 'Elixir of the Mongoose should have 3 days left to sell', ->
      items[2].sellBy.should.equal 3

    it 'Sulfuras, Hand of Ragnaros should have quality 80', ->
      items[3].quality.should.equal 80

    it 'Sulfuras, Hand of Ragnaros should have 0 days left to sell', ->
      items[3].sellBy.should.equal 0

    it 'Backstage passes should have quality 22', ->
      items[4].quality.should.equal 22

    it 'Backstage passes should have 13 days left to sell', ->
      items[4].sellBy.should.equal 13

    xit 'Conjured Mana Cake should have quality 2', ->
      items[5].quality.should.equal 2

    it 'Conjured Mana Cake should have 1 days left to sell', ->
      items[5].sellBy.should.equal 1

