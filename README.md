Contextual Neural Network Layer with Context Tree Management

This project implements a custom neural network layer, ContextualLayer, that manages a context tree structure for generating, updating, and tracking context clues across nodes. The context tree provides persistent, context-sensitive data that can be used to improve model performance across sessions.

Each node in the context tree represents a “context clue” with an associated accuracy weight. The layer supports automated versioning, pruning, and metadata logging to help track context tree evolution during training.

Features

	•	Context Tree Structure: Each node has a context clue, a weight, and references to parent and child nodes. Nodes can be created, edited, or deleted based on training data.
	•	Automated Versioning and Saving: Saves the context tree every n epochs with timestamp-based versioning, retaining only the latest versions for storage efficiency.
	•	Pruning of Low-Weight Nodes: Automatically removes low-weight nodes to keep the context tree focused and efficient.
	•	Logging and Metadata Tracking: Logs the structure of the context tree and tracks additional metadata (e.g., accuracy, loss) to help analyze saved versions.

Installation

Requirements

	•	Python 3.7+
	•	PyTorch 1.7+
	•	Required libraries: pickle, datetime, os, logging

Getting Started

	1.	Clone the Repository:

git clone https://github.com/your-username/contextual-layer.git
cd contextual-layer


	2.	Install Requirements:
	•	Ensure PyTorch and other dependencies are installed:

pip install torch



Usage

1. Initializing ContextualLayer

Create a ContextualLayer instance, specifying input/output dimensions, pruning thresholds, and save intervals:

from contextual_layer import ContextualLayer

# Initialize the custom layer with configuration options
layer = ContextualLayer(
    input_size=128,                    # Input dimension size
    output_size=64,                    # Output dimension size
    prune_weight_threshold=2.0,        # Prune nodes with weight below threshold
    save_interval=5,                   # Save every 5 epochs
    max_saved_versions=3               # Keep only the 3 most recent versions
)

2. Loading the Latest Context Tree

Load the most recent saved context tree version to continue training with the latest context:

# Load the latest context tree from previous training sessions
layer.load_latest_context_tree("context_tree")

3. Training and Saving with Metadata

During training, update the context tree, prune nodes, and save with performance metadata (e.g., accuracy, loss) every few epochs:

for epoch in range(num_epochs):
    # Forward pass, loss calculation, etc.
    # Calculate example metrics (replace with actual values)
    accuracy = 0.85
    loss = 0.3

    # Prune and log tree at each epoch
    layer.prune_context_tree()
    layer.log_tree_structure()

    # Automated save every `save_interval` epochs with metadata
    layer.automated_save("context_tree", additional_metadata={"accuracy": accuracy, "loss": loss})

4. Viewing Logs and Metadata

All context tree modifications and metadata are saved in context_tree_metadata.log:
	•	Save and Deletion Logs: Track each version saved or deleted, along with timestamps.
	•	Performance Metadata: Store model performance metrics for each version.

Configuration Options

	•	prune_weight_threshold: The minimum weight a node must have to remain in the tree. Nodes with weights below this threshold are deleted.
	•	save_interval: The number of epochs between each save. For example, save_interval=5 saves every 5 epochs.
	•	max_saved_versions: Maximum number of context tree versions to retain. Older versions are deleted to free up storage.

Example Project Structure

contextual-layer/
├── contextual_layer.py          # Main code for ContextualLayer and ContextTree
├── README.md                    # Project documentation
└── context_tree_metadata.log    # Logs for saved versions and metadata

Contributing

Contributions are welcome! To contribute:
	1.	Fork the repository.
	2.	Create a feature branch (git checkout -b feature/YourFeature).
	3.	Commit your changes (git commit -m 'Add feature').
	4.	Push to the branch (git push origin feature/YourFeature).
	5.	Create a new Pull Request.

License

This project is licensed under the MIT License.

Feel free to customize any part of this README, such as the repository name or additional configuration options, before adding it to your GitHub repo.
