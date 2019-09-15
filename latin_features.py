from qcrit.textual_feature import textual_feature, setup_tokenizers

setup_tokenizers(terminal_punctuation=('.', '?'))

@textual_feature()
def test_feature(text):
	return 0
