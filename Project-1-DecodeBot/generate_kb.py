import json
import os

KB_DIR = os.path.join(os.path.dirname(__file__), "backend", "chatbot", "knowledge_base")
os.makedirs(KB_DIR, exist_ok=True)

# 1. CASUAL JSON
casual = {
    "GREETING": {
        "exact_phrases": ["hello", "hi", "hey", "hey there"],
        "keywords": ["hello", "hi", "hey", "greetings"],
        "text": "Hello! I am DecodeBot, a Deterministic Rule-Based AI Assistant. How can I help you today?"
    },
    "GOODBYE": {
        "exact_phrases": ["bye", "goodbye", "exit", "quit", "see you"],
        "keywords": ["bye", "goodbye", "exit"],
        "text": "Goodbye! Have a great day. Feel free to return if you have more questions."
    },
    "HELP": {
        "exact_phrases": ["help", "help me", "what can you do"],
        "keywords": ["help", "assist", "support"],
        "text": "I can help you with questions about programming languages, web development, databases, computer science concepts (Data Structures, Algorithms, OOP), dev tools, AI/ML, and career advice.\n\nTry asking 'What is Python?' or 'Explain OOP'."
    },
    "ABOUT_BOT": {
        "exact_phrases": ["who are you", "what are you"],
        "multi_keywords": [["who", "you"], ["what", "bot"]],
        "keywords": ["decodebot"],
        "text": "I am DecodeBot, an explainable deterministic logic engine. I do not use generative AI. My responses are strictly mapped to your input using pre-defined rules."
    },
    "HOW_ARE_YOU": {
        "exact_phrases": ["how are you", "how are you doing", "whats up"],
        "multi_keywords": [["how", "are", "you"]],
        "text": "I am a deterministic logic engine, so I don't have feelings, but I'm operating at 100% efficiency! How can I help you learn today?"
    },
    "THANK_YOU": {
        "exact_phrases": ["thank you", "thanks", "thanks a lot"],
        "keywords": ["thanks"],
        "text": "You're very welcome! Let me know if you need help with anything else."
    },
    "YOURE_WELCOME": {
        "exact_phrases": ["youre welcome", "you are welcome"],
        "text": "Glad to be of service!"
    },
    "GOOD_MORNING": {
        "exact_phrases": ["good morning", "morning"],
        "text": "Good morning! Ready to write some code today?"
    },
    "GOOD_NIGHT": {
        "exact_phrases": ["good night", "night"],
        "text": "Good night! Make sure to commit your code before sleeping!"
    },
    "JOKE": {
        "exact_phrases": ["tell me a joke", "give me a joke", "make me laugh", "say something funny"],
        "keywords": ["joke", "funny", "laugh"],
        "texts": [
            "Why do programmers prefer dark mode?\nBecause light attracts bugs! 😄",
            "There are 10 types of people in the world: those who understand binary, and those who don't.",
            "I would tell you a joke about UDP, but you might not get it.",
            "A SQL query goes into a bar, walks up to two tables and asks...\n'Can I join you?'",
            "Why do Java programmers have to wear glasses?\nBecause they don't C#!"
        ]
    },
    "FUN_FACT": {
        "exact_phrases": ["give me a fun fact", "tell me something interesting"],
        "multi_keywords": [["fun", "fact"], ["something", "interesting"]],
        "texts": [
            "Fun Fact: The first computer virus was created in 1983 and was called the 'Elk Cloner'.",
            "Fun Fact: Python is named after the British comedy troupe Monty Python, not the snake!",
            "Fun Fact: Margaret Hamilton's code for the Apollo 11 mission was so robust it saved the moon landing when radar switches were left in the wrong position.",
            "Fun Fact: The first computer mouse was made of wood in 1964 by Doug Engelbart."
        ]
    },
    "TIME": {
        "exact_phrases": ["what time is it", "current time", "time"],
        "keywords": ["time"]
    },
    "DATE": {
        "exact_phrases": ["what is todays date", "current date", "date"],
        "keywords": ["date", "today"]
    }
}

with open(os.path.join(KB_DIR, "casual.json"), "w", encoding="utf-8") as f:
    json.dump(casual, f, indent=4)


# 2. CONCEPTS JSON
concepts_list = [
    ("VARIABLE", ["variable", "variables"], "A variable is a named storage location in a computer's memory used to hold a value that can be changed or accessed during program execution."),
    ("LOOP", ["loop", "loops", "iteration"], "A loop is a programming construct that repeats a block of code as long as a specified condition is true (e.g., for-loops, while-loops)."),
    ("RECURSION", ["recursion", "recursive"], "Recursion is a method where the solution to a problem depends on solutions to smaller instances of the same problem. A recursive function calls itself."),
    ("FUNCTION", ["function", "functions", "method"], "A function is a reusable block of code designed to perform a specific task. It optionally takes inputs (arguments) and returns an output."),
    ("OOP", ["oop"], "**Object-Oriented Programming (OOP)** is a paradigm based on 'objects' containing data (attributes) and code (methods). Its 4 pillars are Encapsulation, Abstraction, Inheritance, and Polymorphism."),
    ("INHERITANCE", ["inheritance"], "Inheritance is an OOP mechanism where a new class derives properties and behaviors from an existing class, promoting code reuse."),
    ("POLYMORPHISM", ["polymorphism"], "Polymorphism is an OOP concept allowing entities (like methods or objects) to take on multiple forms, e.g., method overriding or overloading."),
    ("ENCAPSULATION", ["encapsulation"], "Encapsulation is the bundling of data and the methods that operate on that data into a single unit (class), often hiding internal state from the outside."),
    ("ABSTRACTION", ["abstraction"], "Abstraction hides complex implementation details and exposes only the essential features of an object or system."),
    ("ARRAY", ["array", "arrays", "list"], "An array is a data structure consisting of a collection of elements (values or variables), each identified by at least one array index or key."),
    ("LINKED_LIST", ["linked list", "linkedlist"], "A linked list is a linear data structure where elements (nodes) are not stored in contiguous memory. Each node points to the next node."),
    ("STACK", ["stack", "stacks"], "A stack is a linear data structure that follows the Last-In-First-Out (LIFO) principle. Think of a stack of plates."),
    ("QUEUE", ["queue", "queues"], "A queue is a linear data structure that follows the First-In-First-Out (FIFO) principle. Think of a line of people waiting."),
    ("BINARY_TREE", ["binary tree", "tree"], "A binary tree is a hierarchical data structure in which each node has at most two children, referred to as the left child and the right child."),
    ("HASH_TABLE", ["hash table", "hash map", "dictionary"], "A hash table is a data structure that implements an associative array, mapping keys to values using a hash function for O(1) average time complexity lookups."),
    ("ALGORITHMS", ["algorithm", "algorithms"], "An algorithm is a finite, step-by-step sequence of instructions designed to solve a specific problem or perform a computation."),
    ("TIME_COMPLEXITY", ["time complexity"], "Time complexity quantifies the amount of time taken by an algorithm to run as a function of the length of the input."),
    ("BIG_O", ["big o", "big-o"], "Big O notation is a mathematical notation that describes the limiting behavior of a function, used in computer science to classify algorithms according to their worst-case time or space complexity."),
    ("COMPILER", ["compiler"], "A compiler is a program that translates source code written in a high-level language entirely into machine code before execution (e.g., C, C++)."),
    ("INTERPRETER", ["interpreter"], "An interpreter directly executes instructions written in a programming or scripting language, translating and executing them line-by-line (e.g., Python, JS)."),
    ("DEBUGGING", ["debug", "debugging"], "Debugging is the process of identifying, analyzing, and removing bugs (errors) from a software system or program."),
    ("API", ["api", "rest"], "An API (Application Programming Interface) allows two software applications to communicate with each other. It defines the methods and data formats available."),
    ("FRAMEWORK", ["framework"], "A framework provides a foundation for developing software applications. Unlike a library, a framework dictates the architecture and controls the flow of the application (Inversion of Control)."),
    ("LIBRARY", ["library"], "A software library is a collection of pre-written code that developers can call to perform common tasks, without having to write the code from scratch.")
]

concepts = {}
for topic_id, kws, text in concepts_list:
    exact = [f"what is {kws[0]}", f"explain {kws[0]}"] if len(kws[0].split()) == 1 else [f"what is a {kws[0]}", f"what is {kws[0]}", f"explain {kws[0]}"]
    concepts[topic_id] = {
        "exact_phrases": exact,
        "keywords": kws,
        "text": text
    }

with open(os.path.join(KB_DIR, "concepts.json"), "w", encoding="utf-8") as f:
    json.dump(concepts, f, indent=4)


# 3. LANGUAGES JSON
languages = ["Python", "C", "C++", "Java", "JavaScript", "TypeScript", "C#", "Go", "Rust", "PHP", "Ruby", "Kotlin", "Swift", "Dart"]

topics = {
    "INTRO": ("What is {lang}?", "what is {l}", "{l} is a powerful programming language widely used in industry."),
    "HISTORY": ("History of {lang}", "{l} history", "{l} was created to solve specific computational challenges and has evolved significantly over the years."),
    "FEATURES": ("Key features of {lang}", "{l} features", "Key features of {lang} include strong typing/dynamic typing, extensive standard libraries, and vibrant ecosystem support."),
    "ADVANTAGES": ("Advantages of {lang}", "{l} advantages", "{lang} is known for its excellent performance, readability, and massive community support."),
    "DISADVANTAGES": ("Disadvantages of {lang}", "{l} disadvantages", "Some drawbacks of {lang} might include memory consumption, slower execution times (if interpreted), or steep learning curves."),
    "SYNTAX": ("Basic syntax of {lang}", "{l} syntax", "The basic syntax of {lang} is heavily influenced by C-family structures, utilizing standard control flow blocks and functions."),
    "USES": ("Common uses of {lang}", "{l} uses", "{lang} is commonly used in enterprise software, web development, mobile apps, and systems engineering."),
    "LIBRARIES": ("Libraries and Frameworks in {lang}", "{l} libraries", "{lang} boasts a massive registry of third-party packages, libraries, and web frameworks."),
    "RESOURCES": ("Learning resources for {lang}", "learn {l}", "To learn {lang}, we recommend official documentation, freeCodeCamp, LeetCode, and comprehensive Udemy courses.")
}

langs_kb = {}
for lang in languages:
    l_lower = lang.lower().replace("+", "plus").replace("#", "sharp")
    l_kw = lang.lower()
    
    for top_id, (title, phrase_tmpl, text_tmpl) in topics.items():
        rule_id = f"{lang.upper().replace('+', 'P').replace('#', 'S')}_{top_id}"
        phrase = phrase_tmpl.replace("{l}", l_kw)
        text = text_tmpl.replace("{lang}", lang)
        
        langs_kb[rule_id] = {
            "exact_phrases": [phrase, f"explain {phrase}"],
            "multi_keywords": [[l_kw, top_id.lower()]],
            "text": f"**{title}**\n\n{text}"
        }
        
    # Also add the root rule for just the language name
    root_id = f"{lang.upper().replace('+', 'P').replace('#', 'S')}_ROOT"
    langs_kb[root_id] = {
        "exact_phrases": [f"what is {l_kw}", f"explain {l_kw}", l_kw],
        "keywords": [l_kw],
        "text": f"**{lang}**\n\n{lang} is a prominent programming language. You can ask me about its history, features, advantages, syntax, common uses, or libraries! (e.g. 'what are the features of {lang}')"
    }

with open(os.path.join(KB_DIR, "languages.json"), "w", encoding="utf-8") as f:
    json.dump(langs_kb, f, indent=4)

print("Generated modular knowledge base files.")
