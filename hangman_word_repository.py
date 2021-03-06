# words is a copy-pasted string of 1000 words
# words_list is a 1000 word list created from that string

words = """brother
    chief
    trap
    absent
    shake
    found
    capable
    defiant
    green
    insect
    owe
    type
    concern
    humor
    assorted
    healthy
    eminent
    quirky
    waste
    locket
    ocean
    pushy
    bite
    special
    industrious
    quarter
    grubby
    soggy
    waiting
    coach
    connect
    flavor
    heavy
    bee
    gigantic
    religion
    post
    slope
    dynamic
    nail
    abounding
    instinctive
    lumber
    harmonious
    reaction
    hungry
    ready
    glass
    legal
    bead
    delicious
    glow
    list
    busy
    bare
    harmony
    drip
    wink
    summer
    egg
    loose
    unbiased
    tin
    nostalgic
    lopsided
    earthy
    thinkable
    fit
    common
    squash
    plain
    label
    cart
    honorable
    stop
    fertile
    boast
    sheep
    deranged
    arrest
    curious
    plantation
    lucky
    odd
    bedroom
    bit
    one
    steel
    bumpy
    perform
    brush
    giraffe
    helpful
    care
    swanky
    hang
    tent
    alluring
    kittens
    fast
    impress
    arm
    sin
    smelly
    nimble
    animated
    short
    knotty
    provide
    adorable
    treatment
    butter
    pen
    rush
    various
    supply
    ignorant
    tramp
    mind
    moan
    crime
    exercise
    new
    flock
    talk
    jewel
    jobless
    calendar
    value
    grab
    wild
    stiff
    barbarous
    plane
    charming
    frog
    devilish
    brash
    mammoth
    coal
    food
    glorious
    babies
    voyage
    aboriginal
    dust
    digestion
    rail
    parched
    psychotic
    panicky
    gabby
    honey
    graceful
    outgoing
    upbeat
    flat
    astonishing
    birthday
    acoustics
    rapid
    border
    efficacious
    icky
    number
    smoke
    correct
    painful
    appreciate
    blind
    fire
    industry
    pail
    valuable
    club
    island
    pot
    switch
    eatable
    neighborly
    texture
    bell
    pricey
    spoon
    farm
    accept
    escape
    melt
    vanish
    ice
    sleepy
    harbor
    earth
    rescue
    zealous
    pickle
    gifted
    letter
    flap
    delirious
    clear
    absurd
    chess
    momentous
    power
    interesting
    unwieldy
    frail
    liquid
    songs
    fly
    savory
    prevent
    beam
    paste
    selective
    park
    share
    obeisant
    oafish
    cooing
    alert
    spiteful
    ruddy
    chew
    stormy
    sassy
    preserve
    invincible
    thankful
    realise
    tip
    responsible
    hair
    limping
    dear
    ubiquitous
    linen
    cracker
    even
    jittery
    wrathful
    foolish
    unadvised
    young
    mix
    tenuous
    fragile
    receipt
    functional
    discreet
    highfalutin
    unknown
    naive
    force
    calculator
    melodic
    fold
    fry
    magenta
    company
    sordid
    misty
    accessible
    tease
    compare
    end
    nine
    mist
    absorbing
    hanging
    peep
    deadpan
    run
    neat
    boorish
    please
    scarf
    sparkling
    eight
    furtive
    expand
    sisters
    noise
    admit
    offer
    next
    acidic
    potato
    bomb
    serious
    boy
    flowery
    horse
    halting
    fallacious
    basket
    bustling
    muddled
    decay
    argument
    coordinated
    lame
    drain
    support
    offbeat
    guarded
    homeless
    elegant
    direction
    confess
    ring
    salty
    six
    handsomely
    knowledge
    periodic
    wary
    fruit
    cows
    shiver
    useless
    dry
    befitting
    cub
    roasted
    hallowed
    breakable
    complain
    space
    innocent
    tame
    habitual
    chilly
    van
    sidewalk
    pale
    mouth
    skinny
    muddle
    mighty
    sign
    disagree
    material
    axiomatic
    juggle
    paltry
    disastrous
    plan
    guard
    political
    tested
    waves
    languid
    rabbits
    fog
    yoke
    flashy
    turn
    broad
    great
    cycle
    caring
    tightfisted
    rod
    wriggle
    minister
    ugliest
    wall
    zoo
    crook
    sheet
    advertisement
    jog
    regret
    spring
    sort
    puffy
    kind
    trick
    unnatural
    blade
    mark
    crawl
    rob
    alcoholic
    tawdry
    trade
    approve
    icy
    left
    uneven
    military
    cent
    exotic
    earsplitting
    tiresome
    destruction
    market
    sound
    safe
    follow
    fierce
    airplane
    rainy
    window
    pie
    corn
    cumbersome
    education
    silky
    insurance
    statuesque
    tranquil
    poor
    minute
    laugh
    notice
    doubt
    silent
    obsequious
    planes
    fat
    page
    sack
    little
    nippy
    quill
    cynical
    gate
    marvelous
    impartial
    noisy
    ablaze
    children
    cloth
    true
    murder
    subsequent
    suspend
    white
    fine
    title
    seed
    poke
    detect
    deep
    knowledgeable
    disappear
    decision
    library
    flight
    ambiguous
    adjustment
    purple
    welcome
    girls
    crabby
    quiet
    fixed
    terrify
    toothbrush
    bright
    spare
    right
    overt
    interest
    inexpensive
    foregoing
    productive
    telling
    high
    awake
    scatter
    beautiful
    heartbreaking
    surround
    aboard
    feigned
    detail
    juvenile
    serve
    shiny
    ban
    malicious
    sky
    invent
    superb
    smell
    faint
    frantic
    low
    head
    peaceful
    rambunctious
    wonderful
    dislike
    mysterious
    can
    excited
    super
    knot
    tooth
    clover
    bird
    cake
    hour
    actually
    respect
    phone
    mint
    panoramic
    itchy
    use
    play
    print
    wrench
    dramatic
    drunk
    caption
    adventurous
    brief
    spiders
    government
    secretive
    light
    school
    cactus
    water
    business
    disturbed
    salt
    curly
    whispering
    adjoining
    shop
    form
    license
    depressed
    tug
    groovy
    belief
    avoid
    unlock
    chin
    fascinated
    breath
    carve
    fluttering
    hat
    tasty
    electric
    trace
    comparison
    premium
    learned
    colossal
    voiceless
    stir
    elbow
    grandiose
    holistic
    abstracted
    horses
    hum
    dusty
    grate
    burly
    discover
    wealth
    distance
    aromatic
    fix
    embarrass
    bait
    righteous
    sense
    tiger
    control
    fetch
    strip
    utopian
    enter
    simple
    unit
    perpetual
    gaudy
    determined
    dark
    cherries
    roof
    airport
    mushy
    mere
    door
    army
    promise
    available
    cloistered
    ugly
    punishment
    string
    cannon
    reduce
    wheel
    polite
    important
    far
    deceive
    kiss
    hurried
    sofa
    underwear
    mountain
    crib
    didactic
    fearless
    different
    silk
    cable
    toad
    hop
    ragged
    rhetorical
    pleasure
    unwritten
    snakes
    rhythm
    swim
    teaching
    joyous
    innate
    scarce
    quizzical
    legs
    fretful
    peace
    nondescript
    equal
    hard
    cattle
    whip
    remarkable
    numerous
    male
    men
    sad
    succeed
    reply
    laughable
    pest
    boring
    request
    discovery
    sock
    snow
    cool
    recess
    hunt
    pigs
    windy
    tow
    save
    existence
    tongue
    pedal
    lush
    impossible
    elderly
    stage
    argue
    smoggy
    voice
    automatic
    measly
    furniture
    squirrel
    wool
    noxious
    peck
    distribution
    bells
    plausible
    income
    yellow
    wonder
    berserk
    unsightly
    unable
    loss
    mindless
    health
    brown
    woman
    achiever
    puzzled
    giant
    undesirable
    meal
    extend
    oceanic
    tacit
    thick
    concentrate
    free
    symptomatic
    living
    evanescent
    cute
    reward
    team
    divide
    moon
    oval
    trail
    meeting
    intend
    humdrum
    help
    awful
    spiky
    rot
    second
    toes
    release
    condemned
    marry
    steadfast
    science
    heal
    step
    greasy
    work
    hulking
    tasteless
    comfortable
    silver
    four
    ad hoc
    offend
    hose
    worried
    scare
    dysfunctional
    uncle
    repeat
    amuse
    arrange
    approval
    freezing
    twig
    north
    careless
    yard
    cry
    imminent
    sun
    violent
    romantic
    humorous
    hook
    coherent
    interfere
    search
    party
    huge
    protest
    hurt
    flame
    encouraging
    air
    spray
    rhyme
    nosy
    dinner
    giants
    squalid
    cellar
    racial
    remind
    sophisticated
    direful
    hellish
    reminiscent
    stretch
    drop
    finger
    aloof
    plant
    furry
    front
    null
    roomy
    waggish
    pull
    utter
    long
    gratis
    toothpaste
    puzzling
    stroke
    cheese
    live
    bump
    colour
    easy
    cluttered
    quick
    drawer
    file
    hug
    spotted
    screw
    mundane
    fax
    tremble
    vein
    sleep
    real
    plough
    teeny
    wine
    debt
    draconian
    stove
    kill
    cushion
    curvy
    gold
    lie
    ancient
    substance
    tangible
    vessel
    grease
    claim
    announce
    pastoral
    exist
    hissing
    moor
    present
    look
    unarmed
    queue
    amusing
    incredible
    succinct
    hateful
    snatch
    married
    measure
    snails
    jail
    travel
    march
    gamy
    donkey
    bleach
    pies
    degree
    toothsome
    receptive
    territory
    ghost
    staking
    bent
    excellent
    dad
    raspy
    snore
    rely
    crate
    tempt
    lake
    steer
    magic
    bulb
    paddle
    bless
    lunchroom
    arrogant
    purpose
    range
    divergent
    youthful
    taste
    relax
    river
    activity
    hushed
    base
    half
    forgetful
    wave
    chase
    cars
    ossified
    vest
    vegetable
    haircut
    guitar
    three
    ambitious
    infamous
    identify
    beginner
    aggressive
    spark
    lavish
    prickly
    yawn
    abandoned
    magnificent
    normal
    field
    jeans
    vengeful
    red
    unequaled
    testy
    include
    combative
    sand
    wipe
    wise
    rich
    drown
    finicky
    cover
    weather
    tedious
    dirty
    defeated
    scrawny
    untidy
    thought
    pour
    heavenly
    remove
    borrow
    wakeful
    carpenter
    refuse
    wander
    man
    amazing
    land
    delightful
    wide
    scent
    crooked
    tense
    thirsty
    minor
    unusual
    black
    transport
    wistful
    dress
    polish
    aunt
    tank
    volcano
    tall
    sea
    blink
    year
    flimsy
    grip
    fireman
    invention
    round
    fuel
    shoe
    irritate
    parsimonious
    yak
    return
    public
    messy
    advice
    account
    previous
    glossy
    hate
    prefer
    slap
    teeth
    sneaky
    clever
    type
    disagree
    receipt
    rampant
    capricious
    fragile
    loose
    station
    control"""

words = words.replace(" ", "1")
words = words.replace("\n", "1")
word_list = words.split("11111")

