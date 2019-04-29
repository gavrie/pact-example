To run the consumer tests and create a Pact file:

    pytest -v consumer

To run the provider and verify the pact against it:
    
In one terminal window:

    FLASK_APP=provider/provider.py flask run

In another window:
    pact-verifier --pact-url consumer-provider.json --provider-base-url http://localhost:5000
