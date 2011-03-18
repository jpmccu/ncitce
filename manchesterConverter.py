from org.coode.owlapi.manchesterowlsyntax import ManchesterOWLSyntaxOntologyFormat
from org.semanticweb.owlapi.apibinding import OWLManager

import sys

from java.io import File

from org.semanticweb.owlapi.io import *
from org.semanticweb.owlapi.model import *

manager = OWLManager.createOWLOntologyManager()
inputFile = File(sys.argv[1])
outputFile = File(sys.argv[2])

ontology = manager.loadOntologyFromOntologyDocument(inputFile)
format = manager.getOntologyFormat(ontology)

manSyntaxFormat = ManchesterOWLSyntaxOntologyFormat()
if format.isPrefixOWLOntologyFormat():
    manSyntaxFormat.copyPrefixesFrom(format.asPrefixOWLOntologyFormat())

manager.saveOntology(ontology, manSyntaxFormat, IRI.create(outputFile.toURI()));
