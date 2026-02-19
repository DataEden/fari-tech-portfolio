# define function header for filter_nondigits() function.
def filter_nondigits(data: list) -> list:
    """
    filter_nondigits() takes in a list of strings and filters
    out all strings that include non-integer elements.

    Args:    
        data (list): A list of strings elements.

    Returns:
        list: A list of strings containing type-int elements.          
    """    
    
    if not data:
        return []
  
    clean_list = []  # Initialize empty list to store permissible elements.
    for val in data:  # Iterate over list of strings.
        clean_element = val.strip()  # remove newline characters from the string.
        if clean_element.isdigit():  # Check if element is a digit.
            clean_list.append(int(clean_element))  # Convert string to permissible elements and append list.
    return clean_list  # Return list of int/permissible elements.
    