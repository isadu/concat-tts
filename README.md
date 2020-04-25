# concat-tts
Simple concatenative text-to-speech in Python

[x] Stage 0: letters to sequence of 1-sec letter sounds
[x] Stage 1: letters to sequence of properly trimmed letter sounds
	- bonus: added spaces
[x] Stage 2: word to ARPAbet to sequence of ARPAbet sounds
	- pronouncing dictionary lookup
	- switch to allow one-or-more-char codes
[x] Stage 3: ...with stress
	- CMU pronouncing dictionary lookup
[ ] Stage 4: common clusters
	- technical prereq for 4-7: neighbor-aware processing
	- phase 1 - affricate for ts
	- phase 2 - s[ptkmnl], s[ptk]r, [ptkbdgfTHSH]r, spl, [pkbgf]l, [stk]w
	- phase 3 - sf, dw, skw, sfr, codas
[ ] Stage 5: ...with phonetic detail
	- dark/clear L
	- syllabics
	- aspiration
	- rhotacization
	- flapping
	- unreleased stops
[ ] Stage 6: cross-word-boundary rules applied
[ ] Stage 7: context-aware recordings/segment recordings
	- ideally hit side goal first
	- (ata aba the a's are all different, or a[t] + ta)
[ ] Stage 8: questions and exclamations 
	- manipulate pitch?

Side goals:
[ ] Automate more of the sound file process
	- Praat script?

