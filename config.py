import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-key-change-me-in-production'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///fitness_coach.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Configuration Amazon Bedrock
    AWS_REGION = os.environ.get('AWS_REGION') or 'us-east-1'
    
    # ID du modèle Claude 3.7 Sonnet
    BEDROCK_MODEL_ID = os.environ.get('BEDROCK_MODEL_ID') or 'us.anthropic.claude-3-7-sonnet-20250219-v1:0'

    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID') or "ASIA4PRNH3P2JLGUKF2J"
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY') or "sYndtvnV7kJE/PKuJrDSAR9jCP5wu7rMqESWj3Mw"
    AWS_SESSION_TOKEN = os.environ.get('AWS_SESSION_TOKEN') or "IQoJb3JpZ2luX2VjEOb//////////wEaCXVzLWVhc3QtMSJIMEYCIQDX9T5sfa0yTEOMrJA/WvaeY0G6NZqfd+hT1Y1+GE2NFQIhAJr3vOjIUmI41q2lmz8ot/ZLcNSLvgmAFq/Fl8XZ52CAKrgDCI///////////wEQARoMODU4MDE0NjA0Mjc2IgxwsNo4Y2GLRmUecTYqjAPO6dYWNHUyi2u8i4s9sfEDI7yXPyLlPepWm+oGJsYan6w04aJiht7N62G6zMqOeoVYXLQ9R36RfsSr84nqjIzVqUQApm6+vRle1zYAFXyqk6XeG9aIH6BnfSWoSyXXGPbxL2VvG226IkGpTDz5GwbMS7eTYE9oOgQcdTxPD0+YyAcrufp0RJcWLdt31G5EwaREHfxncWcWg0iXbjSign5u6K7JWc2bWFDN8XLLwseBiqksz4LFu7vHFZ3kMHfsOwpgg7/Wmr51BQODwrTUvZANA5muYubgtcill3g1DNirWSzH/r5U3emh2wJZHuh6V9nRVcnewy6bzYppG8pcrkwUOXqrj2BtyStUjQZ4l3Krcm/XYOQ0pm/CmGJOw8hHlNgJudU5OtrwWsgbLxSmMQU5lqistE4yWxvEhaLSlMp/oPx3wdXz3WqK/0DpMpWJ5Q0n9I0GS9md8TzqSKPtbEyopC0xjibtQ8vcXc2GOKh6SAAMUWMs/CMc3mfkbp4aR0bNvYDbw9hAxJgKk7cwgIz4wAY6nAEMLSm4X1nRrRlVSw2lKWiZpy6OAQaoOwob19r9fRXmQwyhtfUq4fr6r2K/GHZfVnGloTj0dA8pj92IYL1bVGaIY93LH78GfPsNrTfjjGtEqkQGRfAwYP9Udfo3NQlF6iAn8RatXQJN9ThQqhuxYcao2OZecSigk3yJGhDNCDiyedTyCJXlYh/JUKp4RrxWTaZDIfrUKJK2CCCRz2I="
    AWS_DEFAULT_REGION = "us-east-1"
    
    # Configuration pour les images
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # Limite la taille des uploads à 16 Mo
    UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'uploads')
    ALLOWED_IMAGE_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp'}
    
    # Configuration pour le redimensionnement des images
    MAX_IMAGE_WIDTH = 1200
    MAX_IMAGE_HEIGHT = 1200
    IMAGE_QUALITY = 85  # Pour les images JPEG
