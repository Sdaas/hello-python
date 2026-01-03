clean:
	@echo "Cleaning up build and test artifacts..."
	rm -rf .pytest_cache
	rm -rf .coverage
	rm -rf htmlcov
	rm -rf coverage.xml
	rm -rf .mutmut-cache
	rm -rf mutatnts
	find . -type d -name "__pycache__" -exec rm -rf {} +
	@echo "Clean complete!"