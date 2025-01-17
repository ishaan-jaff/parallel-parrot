import os
import logging

import pandas as pd  # type: ignore
import parallel_parrot as pp


config = pp.OpenAIChatCompletionConfig(
    openai_api_key=os.environ["OPENAI_API_KEY"],
    model="gpt-3.5-turbo-0613",
)

logging.basicConfig(level=logging.DEBUG)

if __name__ == "__main__":
    input_df = pd.DataFrame(
        {
            "input": [
                "this is a super duper product that will change the world",
                "do not buy this",
            ],
            "source": [
                "amazon",
                "shopify",
            ],
        },
        index=[100, 101],
    )
    (output_df, usage_stats_sum) = pp.run_async(
        pp.parallel_text_generation(
            config=config,
            input_data=input_df,
            prompt_template="""
What is the sentiment of this product review?
POSITIVE, NEUTRAL or NEGATIVE?
product review: ${input}
sentiment:""",
            output_key="sentiment",
        )
    )
    print(repr(output_df))
    print(repr(usage_stats_sum))
