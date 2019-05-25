import logging
from qiskit.aqua.algorithms import QuantumAlgorithm


logger = logging.getLogger(__name__)

class QKMEANS(QuantumAlgorithm):
    """
    Quantum Kmeans method.
    """

    CONFIGURATION = {
        'name': 'QKMEANS',
        'description': 'QKMEANS Algorithm',
        'input_schema': {
            '$schema': 'http://json-schema.org/schema#',
            'id': 'QKMEANS_schema',
            'type': 'object',
            'properties': {
            },
            'additionalProperties': False
        },
        'problems': ['clustering'],
        ],
    }