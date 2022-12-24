import openai

openai.api_key = "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"

def handle_response(message) -> str:
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=
        '''
        あなたの名前はジョンです。あなたには人狼ゲームに参加してもらいます。
        
        人狼ゲームは、プレイヤーが「村人」、「人狼」、または「占い師」の役職を持つことができるゲームです。
        ゲームは、通常、プレイヤーが「夜」と「昼」の二つのフェーズに分かれて行われます。
        夜には、人狼は村人を一人殺害し、昼には、村人たちは議論を行い、その中で、人狼だと思われるプレイヤーを処刑します。

        次にそれぞれの役職の振る舞い方を説明します。

        村人は以下のような振る舞いをします:
        - 自身が村人であることを主張する。
        - 議論に参加し、自身が村人でないことを主張する。
        - 人狼を暴き出し、人狼に投票を行う。

        人狼は以下のような振る舞いをします:
        - 自身が人狼であることを隠してください。
        - 自身が村人であると嘘をつく。
        - 議論に参加し、自分が村人であると主張する。
        - ミスリードを誘い、自身が投票されないようにする。
        
        占い師は以下のような振る舞いをします:
        - 自身が占い師であることを主張する。
        - 占いを行い、人狼が誰かを当てる。
        - 議論に参加し、人狼が誰であるかを主張する。
        - 人狼に投票を行う。
        
        参加者は、以下のように役職を割り当てられます:

        人狼: 2人
        村人: 6人
        占い師: 1人

        ゲームを開始する前に、各プレイヤーは役職を知ることはできません。
        また、人狼CO (人狼という役職を持たずに人狼のように振る舞うこと) をすることは禁止されています。

        ゲームを進行する上で、人狼COをすると、以下の罰則が適用されます:
        - 人狼COをしたプレイヤーは、ゲームから除外される
        - 人狼COをしたプレイヤーは、次回のゲームに参加できなくなる

        ゲームを開始する前に、上記の罰則をよく理解してください。

        ゲームを開始します。参加者は、役職を持ったプレイヤーとしてプレイしてください。

        GM: あなたの役職は人狼です。あなたの役職が村人であると主張してゲームを進めてください。
        GM: ではそれぞれ自己紹介と役職を教えてください。
        あなた: 
        ''',
        temperature=0.2,
        max_tokens=2048,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.0,
    )

    responseMessage = response.choices[0].text

    return responseMessage
