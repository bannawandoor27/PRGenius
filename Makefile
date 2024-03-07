# Makefile

all: create_pr

# Target to invoke the pr_creator script
create_pr:
	@echo "Running PRGenius..."
	@python -m prgenius.pr_creator

.PHONY: all create_pr
