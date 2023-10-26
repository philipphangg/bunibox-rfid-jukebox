APP_NAME := bunibanibox

.PHONY:

## git-crypt ##
decrypt:
	git-crypt unlock ~/git-crypt-${APP_NAME}.private

audio_names_cleanup:
	find audio -depth -name "* *" -execdir bash -c 'pwd; for f in "$@"; do mv -nv "$f" "${f// /_}"; done' dummy {} +
	for i in $( find audio -depth ); do mv -i $i `echo $i | tr 'A-Z' 'a-z'`; done
