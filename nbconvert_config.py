c = get_config()
c.TagRemovePreprocessor.enabled = True
c.TagRemovePreprocessor.remove_input_tags = {'hide_input'}
c.Exporter.preprocessors = ['nbconvert.preprocessors.TagRemovePreprocessor']
