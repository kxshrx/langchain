{
  "title": "Review",
  "type": "object",
  "properties": {
    "id": {
      "type": ["integer", "null"],
      "description": "the id of the reviewer"
    },
    "user": {
      "type": "string",
      "description": "the name ofthe reviewer",
      "default": "Anonymous"
    },
    "keythemes": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "write down all the key themse decribed in review in list"
    },
    "summary": {
      "type": "string",
      "description": "it is the concise and true summary of the review but in a cirsp and shortened way represented in shortened bulletins"
    },
    "sentiment": {
      "type": "string",
      "enum": ["positive", "negative", "netural"],
      "description": "it could be either positive , negative or a neutral review"
    },
    "pros": {
      "type": ["string", "null"],
      "description": "the positives mentioned in the review "
    },
    "cons": {
      "type": ["string", "null"],
      "description": "the negatives mentioned in the review "
    }
  },
  "required": ["keythemes", "summary", "sentiment"]
}
