LEXICON: dict[str, str] = {
        '/start_1': "- - - - - - - - - - - - ",
        '/start_2': 'Hi! \nThis bot can form a possible diagnosis'
        " from the symptoms that you choose. The result of"
        " the bot's work is not a medical diagnosis. "
        "To receive a medical diagnosis and treatment,"
        " you should contact a medical institution.\n"
        "Please click on the button /run_diagnostics if you want"
        " to start a preliminary diagnosis. \n"
        "You can get more information if you send"
        " the /help command.",
        '/help': 'This bot can form a possible diagnosis'
        " from the symptoms that you choose. The result of"
        " the bot's work is not a medical diagnosis. "
        "To receive a medical diagnosis and treatment,"
        " you should contact a medical institution.\n"
        'To start, use the /start command.\n'
        "You can stop the diagnostics at any time"
        " if you send the /cancel command.\n"
        "If you want to send feedback or express"
        " your wishes on the work or interface of the bot,"
        " then send a text message with the word feedback"
        " at the beginning.\n For example:\n"
        "feedback your review.",
        '/cancel': "Diagnostics interrupted \n"
        'To start again, use the /start command',
        'go_diagnostic': 'Choose the symptoms.\n'
        'Add or remove a symptom by clicking on it.\n'
        'Select a list of symptoms if you click &lt&lt  or  &gt&gt.\n'
        'The symptoms keyboard number ',
        'user_symptoms': "\n - - - - - - -\n"
        "You have chosen the symptoms: \n",
        'No disease': 'Not identified. Perhaps you are healthy.',
        'very high probability': 'very high probability',
        'high probability': 'high probability',
        'average probability': 'average probability',
        'low probability': 'low probability',
        'diagnoses_text':  "You may have the diagnoses : \n"
        "(If you want to see a description of the disease"
        " and precautions, click the diseases button.)",
        'repeat_diagnostic': "or let's start a new diagnostic?",
        'return_to_symptoms': 'Return to choose symptoms ',
        'return_to_diagnoses': 'Go back to the diagnoses',
        "get_diagnosis": "Get diagnosis",
        'backward': " << ",
        'forward': " >> ",
        'show_symptoms': "Show your symptons",

}
LEXICON_COMMANDS: dict[str, str] = {
    '/start': 'start of diagnostics',
    '/cancel': 'canceling diagnostics',
    '/help': 'help',
}
