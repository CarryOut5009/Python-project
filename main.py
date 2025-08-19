class RecommendationSystem:
    def __init__(self):
        """
        Initialize the recommendation system with expanded movie and book databases.
        Each major category now contains 15-20 options for comprehensive recommendations.
        """
        # Expanded movie database organized by genre → mood → titles
        self.movies_db = {
            "sci-fi": {
                "action": ["The Matrix", "Inception", "Blade Runner 2049", "Dune (2021)", "Mad Max: Fury Road",
                         "The Fifth Element", "Total Recall (1990)", "Starship Troopers", "Edge of Tomorrow",
                         "Alita: Battle Angel", "The Terminator", "Terminator 2: Judgment Day", "RoboCop (1987)",
                         "District 9", "Looper", "Minority Report", "The Hunger Games", "Elysium"],
                "thought-provoking": ["2001: A Space Odyssey", "Interstellar", "Arrival", "Annihilation",
                                    "Moon (2009)", "Ex Machina", "Her", "Solaris (1972)", "Gattaca",
                                    "Children of Men", "The Martian", "Contact", "Predestination",
                                    "Coherence", "Primer", "The Man from Earth", "Another Earth"],
                "cyberpunk": ["Blade Runner", "Ghost in the Shell (1995)", "Akira", "The Matrix",
                             "Johnny Mnemonic", "Strange Days", "Upgrade", "Altered Carbon (TV series)",
                             "Psycho-Pass (anime)", "Dredd", "Elysium", "Ready Player One"]
            },
            "comedy": {
                "romantic": ["When Harry Met Sally", "Crazy, Stupid, Love", "10 Things I Hate About You",
                           "The Big Sick", "Silver Linings Playbook", "Notting Hill", "Love Actually",
                           "500 Days of Summer", "Bridget Jones's Diary", "The Proposal", "You've Got Mail",
                           "Groundhog Day", "Amélie", "The Princess Bride", "Eternal Sunshine of the Spotless Mind"],
                "dark": ["Dr. Strangelove", "Fargo", "In Bruges", "The Death of Stalin", "American Psycho",
                        "Very Bad Things", "Heathers", "World's Greatest Dad", "Harold and Maude",
                        "Eating Raoul", "The Lobster", "Welcome to the Dollhouse", "Little Miss Sunshine"],
                "slapstick": ["Airplane!", "The Naked Gun", "Dumb and Dumber", "Anchorman",
                             "Step Brothers", "Superbad", "The Hangover", "Bridesmaids",
                             "Hot Fuzz", "Shaun of the Dead", "Monty Python and the Holy Grail",
                             "Spaceballs", "Blazing Saddles", "Young Frankenstein", "The Pink Panther"]
            },
            "horror": {
                "psychological": ["Hereditary", "The Shining", "Get Out", "Rosemary's Baby",
                                "The Babadook", "Black Swan", "The Witch", "It Follows",
                                "The Silence of the Lambs", "Psycho (1960)", "Don't Look Now",
                                "The Others", "Jacob's Ladder", "Session 9", "Perfect Blue"],
                "supernatural": ["The Exorcist", "The Conjuring", "Insidious", "Poltergeist",
                                "The Ring", "Sinister", "The Grudge", "Paranormal Activity",
                                "The Sixth Sense", "Oculus", "The Orphanage", "The Changeling",
                                "Stir of Echoes", "The Others", "The Devil's Backbone"],
                "slasher": ["Halloween (1978)", "A Nightmare on Elm Street", "Friday the 13th",
                           "Scream", "Texas Chainsaw Massacre", "Child's Play", "Hellraiser",
                           "Candyman", "I Know What You Did Last Summer", "The Hills Have Eyes",
                           "Maniac", "Black Christmas", "The Strangers", "You're Next", "Happy Death Day"]
            },
            "drama": {
                "historical": ["Schindler's List", "The Pianist", "12 Years a Slave", "Dunkirk",
                              "The King's Speech", "Glory", "Amadeus", "Lincoln", "The Last Emperor",
                              "Atonement", "The Imitation Game", "The English Patient", "Out of Africa",
                              "Braveheart", "Gandhi", "Lawrence of Arabia"],
                "crime": ["The Godfather", "Goodfellas", "Pulp Fiction", "The Departed",
                          "Scarface", "Heat", "Casino", "American Gangster", "The Untouchables",
                          "L.A. Confidential", "Chinatown", "The Usual Suspects", "Training Day",
                          "No Country for Old Men", "Fargo", "The Town"],
                "coming-of-age": ["The Breakfast Club", "Stand by Me", "Dead Poets Society",
                                 "Boyhood", "Moonlight", "Lady Bird", "The Perks of Being a Wallflower",
                                 "Almost Famous", "Eighth Grade", "The 400 Blows", "American Graffiti",
                                 "Dazed and Confused", "The Way Way Back", "The Spectacular Now", "Booksmart"]
            }
        }

        # Expanded book database organized by genre → subcategory → titles
        self.books_db = {
            "fantasy": {
                "epic": ["The Lord of the Rings", "A Song of Ice and Fire (Game of Thrones)",
                        "The Wheel of Time", "The Stormlight Archive", "The Kingkiller Chronicle",
                        "The First Law", "The Broken Empire", "The Malazan Book of the Fallen",
                        "The Lightbringer Series", "The Realm of the Elderlings", "The Poppy War",
                        "The Priory of the Orange Tree", "The Faithful and the Fallen",
                        "The Dandelion Dynasty", "The Rage of Dragons"],
                "urban": ["American Gods", "Neverwhere", "The Dresden Files", "The Rivers of London",
                         "The Magicians", "The Night Circus", "The Invisible Life of Addie LaRue",
                         "Good Omens", "Stardust", "Jonathan Strange & Mr Norrell",
                         "The Library at Mount Char", "The Golem and the Jinni", "The City We Became",
                         "The Ten Thousand Doors of January", "Vicious (Villains series)"],
                "dark": ["The Black Company", "The Broken Empire", "The First Law", "The Poppy War",
                        "Between Two Fires", "The Library at Mount Char", "The Blade Itself",
                        "Prince of Thorns", "The Darkness That Comes Before", "The Court of Broken Knives",
                        "The Traitor Baru Cormorant", "The Fifth Season", "The Shadow of the Torturer",
                        "The Steel Remains", "Best Served Cold"]
            },
            "science-fiction": {
                "hard": ["Dune", "Foundation", "The Three-Body Problem", "Red Mars", "Seveneves",
                        "Anathem", "The Martian", "Project Hail Mary", "Rendezvous with Rama",
                        "Ringworld", "Blindsight", "The Forever War", "Neuromancer", "Snow Crash",
                        "Cryptonomicon"],
                "cyberpunk": ["Neuromancer", "Snow Crash", "Altered Carbon", "Do Androids Dream of Electric Sheep?",
                             "The Diamond Age", "Count Zero", "Mona Lisa Overdrive", "Hardwired",
                             "Trouble and Her Friends", "Void Star", "The Windup Girl", "River of Gods",
                             "Infomocracy", "Daemon", "The Peripheral"],
                "space-opera": ["Hyperion", "The Expanse series", "Revelation Space", "A Fire Upon the Deep",
                               "The Culture series", "Old Man's War", "The Long Way to a Small, Angry Planet",
                               "Ancillary Justice", "The Sparrow", "The Left Hand of Darkness", "The Dispossessed",
                               "The Moon is a Harsh Mistress", "The Stars My Destination", "A Deepness in the Sky",
                               "House of Suns"]
            },
            "mystery-thriller": {
                "detective": ["The Girl with the Dragon Tattoo", "The Silence of the Lambs", "Gone Girl",
                             "The Big Sleep", "The Maltese Falcon", "The Hound of the Baskervilles",
                             "The No. 1 Ladies' Detective Agency", "In the Woods", "The Cuckoo's Calling",
                             "The Alienist", "The Devotion of Suspect X", "The Bat (Harry Hole series)",
                             "The Snowman", "The Dry", "Still Life"],
                "psychological": ["The Silent Patient", "Sharp Objects", "The Woman in the Window",
                                "Gone Girl", "The Girl on the Train", "Before I Go to Sleep",
                                "The Wife Between Us", "The Last Mrs. Parrish", "The Kind Worth Killing",
                                "Behind Closed Doors", "The Turn of the Key", "The Paris Apartment",
                                "Rock Paper Scissors", "The Push", "The Dinner"],
                "legal": ["The Lincoln Lawyer", "Presumed Innocent", "The Firm", "A Time to Kill",
                         "The Pelican Brief", "Defending Jacob", "The Secret History", "The Good Daughter",
                         "Anatomy of a Murder", "The Rainmaker", "The Whistler", "The Reckoning",
                         "The Client", "The Brass Verdict", "The Guardians"]
            },
            "non-fiction": {
                "science": ["A Brief History of Time", "The Selfish Gene", "Cosmos", "The Demon-Haunted World",
                           "Sapiens", "Homo Deus", "The Gene", "The Emperor of All Maladies", "The Sixth Extinction",
                           "The Body", "The Hidden Life of Trees", "The Order of Time", "Astrophysics for People in a Hurry",
                           "The Elegant Universe", "The Making of the Atomic Bomb"],
                "history": ["Guns, Germs, and Steel", "The Rise and Fall of the Third Reich", "A People's History of the United States",
                           "1491", "The Silk Roads", "SPQR", "The Wright Brothers", "The Warmth of Other Suns",
                           "The Immortal Life of Henrietta Lacks", "Team of Rivals", "The Devil in the White City",
                           "The Radium Girls", "King Leopold's Ghost", "The Splendid and the Vile", "1776"],
                "memoir": ["Educated", "The Glass Castle", "When Breath Becomes Air", "Born a Crime",
                           "Wild", "The Year of Magical Thinking", "Becoming", "Just Kids",
                           "The Liars' Club", "Angela's Ashes", "I Know Why the Caged Bird Sings",
                           "The Color of Water", "Between the World and Me", "Hunger", "Men We Reaped"]
            }
        }

    def recommend_movies(self, genre=None, mood=None, dislikes=None, keywords=None):
        """
        Rule-based movie recommendation engine using IF-THEN logic with expanded database
        """
        recommendations = []
        
        # RULE 1: Genre + Mood combination (primary rule)
        if genre and genre in self.movies_db:
            # Check if genre has subcategories (moods)
            if mood and isinstance(self.movies_db[genre], dict) and mood in self.movies_db[genre]:
                recommendations.extend(self.movies_db[genre][mood])  # IF genre=X AND mood=Y THEN recommend Z
            # Handle genre-only rules (no mood specified)
            elif isinstance(self.movies_db[genre], list):
                recommendations.extend(self.movies_db[genre])
        
        # RULE 2: Keyword-based rules (secondary rules)
        if keywords:
            for keyword in keywords:
                keyword = keyword.lower()
                # Keyword rule for classic movies
                if keyword == "classic":
                    classics = []
                    for genre_data in self.movies_db.values():
                        if isinstance(genre_data, dict):
                            if "classic" in genre_data:
                                classics.extend(genre_data["classic"])
                        elif genre == "classic":
                            classics.extend(genre_data)
                    recommendations.extend(classics)
                # Keyword rule for award-winning movies
                elif keyword == "award-winning":
                    recommendations.extend(["Parasite", "The Godfather", "Schindler's List", 
                                          "No Country for Old Men", "The Shape of Water"])
                # Keyword rule for cult classics
                elif keyword == "cult":
                    recommendations.extend(["The Big Lebowski", "Donnie Darko", "Fight Club",
                                         "The Rocky Horror Picture Show", "Repo Man"])
        
        # RULE 3: Avoidance rules (filter out disliked genres)
        if dislikes:
            for dislike in dislikes:
                if dislike in self.movies_db:
                    # Handle genres with mood subcategories
                    if isinstance(self.movies_db[dislike], dict):
                        for mood_list in self.movies_db[dislike].values():
                            recommendations = [m for m in recommendations if m not in mood_list]  # IF dislike=X THEN remove X
                    # Handle flat genre lists
                    else:
                        recommendations = [m for m in recommendations if m not in self.movies_db[dislike]]
        
        return list(set(recommendations))  # Remove duplicates

    def recommend_books(self, genre=None, length=None, dislikes=None, keywords=None):
        """
        Rule-based book recommendation engine using IF-THEN logic with expanded database
        """
        recommendations = []
        
        # RULE 1: Genre + Length combination (primary rule)
        if genre and genre in self.books_db:
            if length and isinstance(self.books_db[genre], dict) and length in self.books_db[genre]:
                recommendations.extend(self.books_db[genre][length])  # IF genre=X AND length=Y THEN recommend Z
            elif isinstance(self.books_db[genre], list):
                recommendations.extend(self.books_db[genre])
        
        # RULE 2: Keyword-based rules (secondary rules)
        if keywords:
            for keyword in keywords:
                keyword = keyword.lower()
                # Keyword rule for bestsellers
                if keyword == "bestseller":
                    recommendations.extend(["The Da Vinci Code", "The Girl on the Train", "Gone Girl",
                                         "The Silent Patient", "Where the Crawdads Sing"])
                # Keyword rule for modern classics
                elif keyword == "modern-classic":
                    recommendations.extend(["The Goldfinch", "The Road", "The Amazing Adventures of Kavalier & Clay",
                                          "White Teeth", "The Corrections"])
                # Keyword rule for debut novels
                elif keyword == "debut":
                    recommendations.extend(["The Secret History", "To Kill a Mockingbird", "Harry Potter and the Philosopher's Stone",
                                         "The Kite Runner", "The Bell Jar"])
        
        # RULE 3: Avoidance rules (filter out disliked genres)
        if dislikes:
            for dislike in dislikes:
                if dislike in self.books_db:
                    if isinstance(self.books_db[dislike], dict):
                        for length_list in self.books_db[dislike].values():
                            recommendations = [b for b in recommendations if b not in length_list]  # IF dislike=X THEN remove X
                    else:
                        recommendations = [b for b in recommendations if b not in self.books_db[dislike]]
        
        return list(set(recommendations))  # Remove duplicates

    def get_user_input(self):
        """
        Handles user interaction and input collection for the main menu
        """
        print("\n" + "="*50)
        print("WELCOME TO THE RULE-BASED RECOMMENDATION SYSTEM")
        print("="*50)
        print("Choose what you want recommendations for:")
        print("1. Movies")
        print("2. Books")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1, 2, or 3): ").strip()
        
        if choice == "1":
            return self.get_movie_input()
        elif choice == "2":
            return self.get_book_input()
        elif choice == "3":
            print("Thank you for using our recommendation system!")
            exit()
        else:
            print("Invalid choice. Please try again.")
            return self.get_user_input()

    def get_movie_input(self):
        """
        Collects movie-specific preferences using rule-based criteria
        """
        print("\n" + "-"*40)
        print("MOVIE RECOMMENDATION OPTIONS")
        print("-"*40)
        
        print("\nAvailable genres: sci-fi, comedy, horror, drama")
        genre = input("What genre are you interested in? (or 'skip'): ").lower().strip()
        
        print("\nAvailable moods: action, thought-provoking, cyberpunk, romantic, dark, slapstick, psychological, supernatural, slasher, historical, crime, coming-of-age")
        mood = input("What mood are you looking for? (or 'skip'): ").lower().strip()
        
        print("\nAvailable keywords: classic, award-winning, cult")
        keywords = input("Any specific keywords? (comma-separated, or 'skip'): ").lower().strip()
        
        dislikes = input("Any genres you dislike? (comma-separated, or 'skip'): ").lower().strip()
        
        # Process inputs (convert to None if skipped)
        return {
            "type": "movie",
            "genre": genre if genre != "skip" else None,
            "mood": mood if mood != "skip" else None,
            "dislikes": [d.strip() for d in dislikes.split(",")] if dislikes != "skip" else None,
            "keywords": [k.strip() for k in keywords.split(",")] if keywords != "skip" else None
        }

    def get_book_input(self):
        """
        Collects book-specific preferences using rule-based criteria
        """
        print("\n" + "-"*40)
        print("BOOK RECOMMENDATION OPTIONS")
        print("-"*40)
        
        print("\nAvailable genres: fantasy, science-fiction, mystery-thriller, non-fiction")
        genre = input("What genre are you interested in? (or 'skip'): ").lower().strip()
        
        print("\nAvailable subcategories: epic, urban, dark, hard, cyberpunk, space-opera, detective, psychological, legal, science, history, memoir")
        length = input("What subcategory are you looking for? (or 'skip'): ").lower().strip()
        
        print("\nAvailable keywords: bestseller, modern-classic, debut")
        keywords = input("Any specific keywords? (comma-separated, or 'skip'): ").lower().strip()
        
        dislikes = input("Any genres you dislike? (comma-separated, or 'skip'): ").lower().strip()
        
        return {
            "type": "book",
            "genre": genre if genre != "skip" else None,
            "length": length if length != "skip" else None,
            "dislikes": [d.strip() for d in dislikes.split(",")] if dislikes != "skip" else None,
            "keywords": [k.strip() for k in keywords.split(",")] if keywords != "skip" else None
        }

    def run(self):
        """
        Main execution loop implementing the complete rule-based workflow:
        1. Get user input → 2. Apply rules → 3. Show output → 4. Repeat or exit
        """
        print("Initializing Rule-Based Recommendation System...")
        
        while True:
            # STEP 1: Get user input
            user_input = self.get_user_input()
            
            # STEP 2: Apply appropriate rules based on input type
            if user_input["type"] == "movie":
                recommendations = self.recommend_movies(
                    genre=user_input["genre"],
                    mood=user_input["mood"],
                    dislikes=user_input["dislikes"],
                    keywords=user_input["keywords"]
                )
                print("\n" + "="*60)
                print("YOUR MOVIE RECOMMENDATIONS")
                print("="*60)
            else:
                recommendations = self.recommend_books(
                    genre=user_input["genre"],
                    length=user_input["length"],
                    dislikes=user_input["dislikes"],
                    keywords=user_input["keywords"]
                )
                print("\n" + "="*60)
                print("YOUR BOOK RECOMMENDATIONS")
                print("="*60)
            
            # STEP 3: Display output
            if recommendations:
                print(f"\nFound {len(recommendations)} recommendations for you:")
                for i, item in enumerate(recommendations, 1):
                    print(f"{i}. {item}")
            else:
                print("\nNo recommendations match your criteria. Try broadening your search.")
            
            # STEP 4: Continue or exit
            print("\n" + "-"*40)
            again = input("Would you like another recommendation? (yes/no): ").lower().strip()
            if again != "yes":
                print("\nThank you for using the Rule-Based Recommendation System!")
                print("Goodbye!")
                break


# Main execution
if __name__ == "__main__":
    try:
        system = RecommendationSystem()
        system.run()
    except KeyboardInterrupt:
        print("\n\nProgram interrupted. Goodbye!")
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        print("Please restart the program.")