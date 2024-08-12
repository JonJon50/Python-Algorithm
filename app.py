def version_compare(version1, version2):
    # Split the version strings into lists of integers
    v1_parts = list(map(int, version1.split('.')))
    v2_parts = list(map(int, version2.split('.')))

    # Compare corresponding parts of both versions
    for i in range(max(len(v1_parts), len(v2_parts))):
        # Get the parts for the current index, defaulting to 0 if not present
        v1_part = v1_parts[i] if i < len(v1_parts) else 0
        v2_part = v2_parts[i] if i < len(v2_parts) else 0

        if v1_part < v2_part:
            return -1
        elif v1_part > v2_part:
            return 1
    
    # All parts are equal
    return 0

def test_version_compare():
    assert version_compare("2", "2.0.0") == 0
    assert version_compare("2", "2.0.0.1") == -1
    assert version_compare("2.1", "2") == 1
    assert version_compare("2.1.0", "2.1.0.10") == -1
    assert version_compare("1.0.0", "1.0.1") == -1
    assert version_compare("1.2.3", "1.2.3") == 0
    assert version_compare("3.4.5", "3.4.4") == 1
    print("All tests passed!")

test_version_compare()
