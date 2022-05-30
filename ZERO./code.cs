using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class playercontroller : MonoBehaviour
{

    public Rigidbody2D rb;
    public float speed ;
    public float jumpforce;
    public Animator anim;
    public LayerMask ground;
    public Collider2D coll;

    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        Movement();
        SwitchAnim();
    }

    void Movement()
    {
        float horizontalmove;
        horizontalmove=Input.GetAxis("Horizontal");
        float facedirction=Input.GetAxisRaw("Horizontal");
        if (horizontalmove !=0)
        {
            rb.velocity = new Vector2(horizontalmove*speed,rb.velocity.y);
            anim.SetFloat("running",Mathf.Abs(facedirction));
        }
        if (facedirction !=0)
        {
            transform.localScale=new Vector3(facedirction,1,1);
        }

        if(Input.GetButtonDown("Jump"))
        {
            rb.velocity=new Vector2(rb.velocity.x,jumpforce);
            anim.SetBool("jumping",true);
        }

    }

    void SwitchAnim()
    {
        anim.SetBool("idle",false);
        if(anim.GetBool("jumping"))
        {
            if(rb.velocity.y<0)
            {
                anim.SetBool("jumping",false);
                anim.SetBool("falling",true);
            }
        }else if(coll.IsTouchingLayers(ground))
        {
            anim.SetBool("falling",false);
            anim.SetBool("idle",true);
        }
    }
}
