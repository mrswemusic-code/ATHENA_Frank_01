from src.core.router.intent_normalizer import IntentNormalizer



normalizer = IntentNormalizer()



tests = [

    "check my computer",

    "remember this information",

    "play my spotify playlist",

    "search latest technology news",

    "debug my python code"

]



for item in tests:


    result = normalizer.normalize(item)


    print(
        item,
        "=>",
        result
    )
