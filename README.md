Code Dojo 15
============
This is the base code from the 15th meeting of the London Code Dojo in mid Dec 2012. Feel free to play around with it. Please read the file 'Gilded Rose kata.md' for details on what the kata involves and how the exercise is structured. The objective is not just to add a feature to the code, but also to add tests to (bad) legacy code and to refactor the code into something much more maintainable and extensible. Good luck!

Other versions of the Gilded Rose starter code for different languages can be found at:

* C# [link](https://github.com/NotMyself/GildedRose)
* Ruby [link](https://github.com/jimweirich/gilded_rose_kata)
* Java [link](https://github.com/alexaitken/GildedRose_java)
* Python [link]()https://github.com/Kyoku57/gildedRosePythonVersion
* Clojure [link](https://github.com/mjansen401/gilded-rose-clojure)
* Javascript [link](https://github.com/guyroyse/gilded-rose-javascript)

You can run the included code in this project (assuming you have node, coffeescript, mocha and chai installed) with:

    mocha --compilers coffee:coffee-script test-*.coffee

You can install dependencies automatically with:

    npm install

(though you will need mocha and coffeescript installed globally)

I have set up a watchr file (kata.watchr) so that the tests are run automatically every time you save a file in your editor, simply run watchr (if you have it installed) with:
    
    watchr kata.watchr

The source of the kata is the Gilded Rose kata, from [here](http://iamnotmyself.com/2011/02/13/refactor-this-the-gilded-rose-kata/)

I've also linked the [slides]() from the meeting. You can find out more about the London Code Dojo at our [homepage](http://www.meetup.com/London-Code-Dojo/).

This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported license - see [http://creativecommons.org/licenses/by-nc-sa/3.0/](http://creativecommons.org/licenses/by-nc-sa/3.0/)
