export const required = (message = "This field is required") => ({
  required: true,
  message: message,
});

/** Field email validation */
export const checkEmail = (label = "Invalid email.", min = 6, max = 50) => {
  return {
    required: true,
    type: "email",
    message: label,
    min: min, // minimum length of email
    max: max, // maximum length of email
  };
};

/** Field min length validation */
export const minLength = (length: number) => {
  return { min: length, message: `Minimum length is ${length} characters.` };
};

/** Field white validation */
export const whiteSpace = () => {
  return { whitespace: true, message: `Whitespace is not allowed.` };
};
