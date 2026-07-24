from semantic_router import Route, RouteLayer
from semantic_router.encoders import HuggingFaceEncoder


encoder = HuggingFaceEncoder(
    name="sentence-transformers/all-MiniLM-L6-v2"
)


faq = Route(
    name="faq",
    utterances=[
        # Returns
        "What is the return policy?",
        "How do I return a product?",
        "Can I return my order?",
        "I want to return an item",
        "What is your return policy?",

        # Refunds
        "How long does a refund take?",
        "When will I receive my refund?",
        "How do I get a refund?",

        # Delivery
        "How long does delivery take?",
        "When will my order arrive?",
        "What is the delivery time?",
        "How many days does shipping take?",
        "When can I expect my order?",

        # Cancellation
        "Can I cancel my order?",
        "How can I cancel my order?",
        "I want to cancel my order",
        "Can I modify my order?",
        "Can I change my order after placing it?",

        # Tracking
        "How can I track my order?",
        "Where is my order?",
        "How do I check my order status?",

        # Payments
        "What payment methods are accepted?",
        "What payment options do you have?",
        "Can I pay using UPI?",
        "Do you accept cash on delivery?",
        "Can I pay with a credit card?",

        # Discounts/policies
        "Do you offer credit card discounts?",
        "Do I get a discount with HDFC credit card?",
    ]
)


sql = Route(
    name="sql",
    utterances=[
        "Show me Nike shoes",
        "I want to buy Nike shoes",
        "I want Nike shoes with 50 percent discount",
        "Are there shoes under Rs 3000?",
        "Show me shoes below 3000",
        "Do you have formal shoes in size 9?",
        "Are there Puma shoes on sale?",
        "What is the price of Puma running shoes?",
        "Show me Puma shoes",
        "Find Adidas shoes",
        "Show me highly rated shoes",
        "What products are available?",
        "Show me products under Rs 5000",
        "Find products with more than 30 percent discount",
    ]
)


small_talk = Route(
    name="small-talk",
    utterances=[
        "Hi",
        "Hello",
        "Hey",
        "Hey there",
        "Good morning",
        "Good afternoon",
        "Good evening",
        "How are you?",
        "How are you doing?",
        "What's up?",
        "What is your name?",
        "Who are you?",
        "Are you a robot?",
        "Are you an AI?",
        "What are you?",
        "What do you do?",
        "Thank you",
        "Thanks",
        "Bye",
        "Goodbye",
        "See you later",
    ]
)


router = RouteLayer(
    routes=[faq, sql, small_talk],
    encoder=encoder
)


if __name__ == "__main__":
    test_queries = [
        "hello",
        "hi",
        "How long does delivery take?",
        "Can I cancel my order?",
        "How do I return a product?",
        "Show me Nike shoes under 3000",
    ]

    for query in test_queries:
        result = router(query)
        print(query, "->", result.name)
