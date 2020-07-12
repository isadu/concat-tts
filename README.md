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
[X] Stage 4: common clusters
	- [x] technical prereq for 4-7: neighbor-aware processing
	- [x] technical prereq part 2: know what sounds are available
	- [x] phase 1 - affricate for ts
	- [x] phase 2 - s[ptkmnl], s[ptk]r, [ptkbdgfTHSH]r, spl, [pkbgf]l, [stk]w
	- phase 3 - sf, dw, skw, sfr, codas
	- issue - syllable boundaries
[ ] Stage 5: ...with phonetic detail
	- [ ] technical prereq: explicit reference to phones
	- [ ] technical prereq: sensitive to word boundary
	- [ ] phase 1 - liquids 
		i. syllabic at end of word immediately after C
		ii. /l/ velarized after V or before C at end of word
	- [ ] phase 2 - nasals syllabic at end of word immediately after obstruent
	- [ ] phase 3 - aspiration (unaspirated ptk in codas)
	- [ ] phase 4 - nasalization
	- could add, but more difficult: flapping, unreleased stops
	- also possible: dentals, t -> glottal stop
[ ] Stage 6: cross-word-boundary rules applied
	- devoiced obstruents
[ ] Stage 7: context-aware recordings/segment recordings
	- ideally hit side goal first
	- (ata aba the a's are all different, or a[t] + ta)
[ ] Stage 8: questions and exclamations 
	- manipulate pitch?

Side goals:
[ ] Automate more of the sound file process
	- Praat script?

01: stage 3
02: plus ts

Redo: IY0 (osprey), AH0 (glottal stop?? trial)
