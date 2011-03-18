#!/bin/sh

TARGET="Thesaurus.omn"

SRC="Prefixes.omn
Ontololgy.omn
AnnotationProperties.omn
ObjectProperties.omn
Datatypes.omn
DatatypeProperties.omn
Classes.omn
Individuals.omn"

rm -f $TARGET

for file in $SRC; do
	cat src/$file >> $TARGET
done
